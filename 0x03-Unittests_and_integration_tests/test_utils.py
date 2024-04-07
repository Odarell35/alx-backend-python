#!/usr/bin/env python3
"""Module"""

import unittest
from typing import Mapping, Sequence, Any
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """class that inherits from unittest.TestCase"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """testing function"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception_message):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
            self.assertEqual(context.exception, expected_exception_message)


class TestGetJson(unittest.TestCase):
    """class to test get_json"""
     @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, mock_get):
        """test for get_json"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('utils.requests.get', return_value=mock_response):
            result = get_json(test_url)
            mock_response.json.assert_called_once()
            self.assertEqual(result, test_payload)
