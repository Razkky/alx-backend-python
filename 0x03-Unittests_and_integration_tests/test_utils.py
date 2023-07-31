#!/usr/bin/env python3
"""This script test the utils.py module"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """This class test the access_nested_map funciton of the utils module"""

    @parameterized.expand([
        ({"a": 1}, ('a'), 1),
        ({"a": {"b": 2}}, ('a'), {"b": 2}),
        ({"a": {"b": 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(
                                self,
                                nested: Mapping,
                                path: Sequence,
                                expected: Any) -> None:
        """This function tests the access_nested_map fucntion"""
        real_nested_map = access_nested_map(nested, path)
        self.assertEqual(real_nested_map, expected)
