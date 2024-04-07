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
