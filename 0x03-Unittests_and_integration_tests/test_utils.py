#!/usr/bin/env python3
"""Module"""
import unittest
from typing import Mapping, Sequence, Any
from parameterized import parameterized
from utils import access_nested_map


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
     
