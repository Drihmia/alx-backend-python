#!/usr/bin/env python3
"""This module tests the client module."""
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock, Mock
import utils
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """A test cases for the GithubOrgClient class's methods """

    @parameterized.expand([
        ('google', 'https://api.github.com/orgs/google'),
        ('abc', 'https://api.github.com/orgs/abc')
    ])
    @patch('client.get_json')
    def test_org(self, org, arg, mock_org):
        """A test case for org method """
        git_client = GithubOrgClient(org)
        org_resp_mock = git_client.org
        org_resp_mock = git_client.org
        org_resp_mock = git_client.org

        mock_org.assert_called_once_with(arg)

    def test_public_repos_url(self):
        """ A test case for _public_repos_url method """
        mock_payload = {"repos_url": "google"}
        with patch.object(GithubOrgClient, 'org',
                          return_value=mock_payload,
                          new_callable=PropertyMock) as mock_org:
            git_client = GithubOrgClient('google')

            pub_repo = git_client._public_repos_url
            self.assertEqual(pub_repo, mock_payload["repos_url"])

    @patch('client.get_json', return_value=TEST_PAYLOAD[0][1])
    def test_public_repos(self, mock_get_jsonn):
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
    def test_has_license(self, repo, license_key, expected):
        """ A test case for has_license method """
        self.assertEqual(
            utils.access_nested_map(
                repo, ('license', 'key')
            ) == license_key, expected)


@parameterized_class((
    'org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
        (TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1],
         TEST_PAYLOAD[0][2], TEST_PAYLOAD[0][3]),
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.mock_request_get

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    @classmethod
    def mock_request_get(cls, url):
        mock_response = Mock()
        if url == 'https://api.github.com/orgs/google':
            mock_response.json.return_value = cls.org_payload
        elif url == 'https://api.github.com/orgs/google/repos':
            mock_response.json.return_value = cls.repos_payload
        return mock_response

    def test_test(self):
        git_client = GithubOrgClient('google')
        pub_repos = git_client.public_repos()
        self.assertEqual(pub_repos, self.expected_repos)


if __name__ == '__main__':
    unittest.main()
