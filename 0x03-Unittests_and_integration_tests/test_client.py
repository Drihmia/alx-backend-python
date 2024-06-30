#!/usr/bin/env python3
"""This module tests the client module."""
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """ """



    @parameterized.expand([
    ('google', 'https://api.github.com/orgs/google'),
    ('abc', 'https://api.github.com/orgs/abc')
    ])
    @patch('client.get_json')
    def test_org(self, org, arg, mock_org):
        """ """
        git_client = GithubOrgClient(org)
        org_resp_mock = git_client.org
        org_resp_mock = git_client.org
        org_resp_mock = git_client.org

        mock_org.assert_called_once_with(arg)


if __name__ == '__main__':
    unittest.main()
