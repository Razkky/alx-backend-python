#!/usr/bin/env python3
"""This script contain test for client.py"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient, get_json


class TestGithubOrgClient(unittest.TestCase):
    """This class contains test function for GithubOrgclient"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_response):
        """This fucntion tests the org fucntion from client.py"""
        githubcli = GithubOrgClient(org_name)
        githubcli.org()
        mock_response.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_public_repos_url(self, org_name):
        """Test the function client.public_repos_url"""
        mock_payload = {"repos_url": f"https://api.github.com/orgs/{org_name}/repos"}
        with patch.object(GithubOrgClient, "org", return_value=mock_payload):
            githubcli = GithubOrgClient('google')
            githubcli_url = githubcli._public_repos_url
            expected_url = f"https://api.github.com/orgs/{org_name}/repos"
            self.assertEqual(githubcli_url, expected_url)