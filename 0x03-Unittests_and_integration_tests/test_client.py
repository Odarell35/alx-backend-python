#!/usr/bin/env python3
""" Module Tests """


import requests
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
import utils
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
  """class"""
  @parameterized.expand([
        ("google",),
        ("abc",),
    ])
  @patch('client.get_json')
  def test_org(self, org_name, expected_result, mock_get_json):
    """method"""
    get_json.return_value = expected_result
    github_client = GithubOrgClient(org_name)
    result = github_client.org()
    get_patch.assert_called_once_with("https://api.github.com/orgs/" + org_name)
    self.assertEqual(result, expected_result)

  @patch('github_org_client.get_json')
  def test_public_repos_url(self, mock_get_json):
    """test case method"""
    mock_payload = {
            "repos_url": "https://api.github.com/orgs/exampleorg/repos"
        }
    mock_get_json.return_value = mock_payload

    org_client = GithubOrgClient("exampleorg")
    expected_url = "https://api.github.com/orgs/exampleorg/repos"
    self.assertEqual(org_client._public_repos_url, expected_url)

  @patch('github_org_client.GithubOrgClient.get_json')
  def test_public_repos(self, mock_get_json, mock_public_repos_url):
    """test case method"""
    mock_public_repos_url.return_value = "https://api.github.com/orgs/example_org/repos"
    mock_payload = [{"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}]
    mock_get_json.return_value = mock_payload

    github_org_client = GithubOrgClient()
    repos = github_org_client.public_repos()
    mock_public_repos_url.assert_called_once()
    mock_get_json.assert_called_once()

    expected_repos = ["repo1", "repo2", "repo3"]
    self.assertEqual(repos, expected_repos)
