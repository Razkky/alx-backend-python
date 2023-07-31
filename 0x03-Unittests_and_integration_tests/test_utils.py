#!/usr/bin/env python3
"""This script test the utils.py module"""
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize
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
        """This function tests the output of access_nested_map fucntion"""
        real_nested_map = access_nested_map(nested, path)
        self.assertEqual(real_nested_map, expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(
                                        self,
                                        nested: Mapping,
                                        path: Sequence,
                                        wrong_output: Any) -> None:
        """This fucntion tests the exception raised by
           access_nested_map fucntion"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(unittest.TestCase):
    """This class test the utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """This function test the output of the get_json fucntion"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    '''This class test the utils.memoize fucntion'''

    def test_memoize(self):
        """Test memoize fucntion"""

        class TestClass:
            """Test class"""

            def a_method(self):
                """Always Return 42"""
                return 42

            @memoize
            def a_property(self):
                """Always return a_method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_value = test_class.a_property
            real_value = test_class.a_property

            self.assertEqual(real_value, 42)
            patched.assert_called_once()
