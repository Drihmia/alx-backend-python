#!/usr/bin/env python3
"""This module tests the client module."""
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import utils
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """A test cases for the GithubOrgClient class's methods """

    @parameterized.expand([
        ('google', 'https://api.github.com/orgs/google'),
        ('abc', 'https://api.github.com/orgs/abc')
    ])
    @patch('client.get_json')
    def test_org(self, org: str, arg: str, mock_org: Mock) -> None:
        """A test case for org method """
        git_client = GithubOrgClient(org)
        org_resp_mock = git_client.org
        org_resp_mock = git_client.org
        org_resp_mock = git_client.org

        mock_org.assert_called_once_with(arg)

    def test_public_repos_url(self) -> None:
        """ A test case for _public_repos_url method """
        mock_payload = {"repos_url": "google"}
        with patch.object(GithubOrgClient, 'org',
                          return_value=mock_payload,
                          new_callable=PropertyMock) as mock_org:
            git_client = GithubOrgClient('google')

            pub_repo = git_client._public_repos_url
            self.assertEqual(pub_repo, mock_payload["repos_url"])

    @patch('client.get_json', return_value=TEST_PAYLOAD[0][1])
    def test_public_repos(self, mock_get_jsonn: Mock) -> None:
        """ A test case for public_repos method """
        git_client = GithubOrgClient('google')

        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          return_value="""
https://api.github.com/orgs/google/repos""",
                          new_callable=PropertyMock) as r:
            pub_repos = git_client.public_repos()
            expected = TEST_PAYLOAD[0][2]
            self.assertEqual(pub_repos, expected)
            r.assert_called_once()
            mock_get_jsonn.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Dict], license_key: str,
                         expected: bool) -> None:
        """ A test case for has_license method """
        git_client = GithubOrgClient('google')
        self.assertEqual(
            git_client.has_license(
                repo, license_key), expected)


@parameterized_class((
    'org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
        (TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1],
         TEST_PAYLOAD[0][2], TEST_PAYLOAD[0][3]),
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ A class for integration test cases for GithubOrgClient class """
    @classmethod
    def setUpClass(cls) -> None:
        """ A class method to set up the mock get """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.mock_request_get

    @classmethod
    def tearDownClass(cls) -> None:
        """ A class method to stop the patcher """
        cls.get_patcher.stop()

    @classmethod
    def mock_request_get(cls, url: str) -> Mock:
        """ A class method to apply side effect on the mock get """
        mock_response = Mock()
        if url == 'https://api.github.com/orgs/google':
            mock_response.json.return_value = cls.org_payload
        elif url == 'https://api.github.com/orgs/google/repos':
            mock_response.json.return_value = cls.repos_payload
        return mock_response

    def test_public_repos(self) -> None:
        """ A test for public_repos method """
        git_client = GithubOrgClient('google')
        pub_repos = git_client.public_repos()
        self.assertEqual(pub_repos, self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """ A test for has_license method """
        git_client = GithubOrgClient('google')
        app_repos = git_client.public_repos('apache-2.0')
        self.assertEqual(app_repos, self.apache2_repos)
