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
        mock_payload = {
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"}
        with patch.object(GithubOrgClient, "org", return_value=mock_payload):
            githubcli = GithubOrgClient('google')
            githubcli_url = githubcli._public_repos_url
            expected_url = f"https://api.github.com/orgs/{org_name}/repos"
            self.assertEqual(githubcli_url, expected_url)

    @patch('client.get_json',
           return_value=[{"name": "test1", "license": {"key": "mit"}}])
    @patch('client.GithubOrgClient._public_repos_url',
           return_value="https:api.github")
    def test_public_repos(self, mock_url, mock_get_json):
        """Test the fucntion Githuborgclient.public_repos"""
        githubcli = GithubOrgClient('google')
        repos = githubcli.public_repos(license="mit")
        expected_repos = ['test1']
        self.assertEqual(expected_repos, repos)
        mock_get_json.assert_called_once()
