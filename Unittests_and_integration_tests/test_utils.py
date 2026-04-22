#!/usr/bin/env python3

""" Unittests for utils module"""

import unittest
from parameterized import parameterized
from unittest.mock import patch

from utils import access_nested_map, get_json, memoize


def _doc_for_case(func, num, params):
    """Build a descriptive docstring for each parameterized test case."""
    return f"{func.__doc__} [case {num + 1}: args={params}]"


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ], doc_func=_doc_for_case)
    def test_access_nested_map(self, nested_map, path, expected):
        """Ensure access_nested_map returns expected values for valid paths."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ], doc_func=_doc_for_case)
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Ensure access_nested_map raises KeyError on invalid paths."""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests for get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ], doc_func=_doc_for_case)
    def test_get_json(self, test_url, test_payload):
        """Verify get_json proxies requests.get & returns JSON payload."""
        with patch("utils.requests.get") as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests for memoize"""

    def test_memoize(self):
        """Ensure the memoize decorator caches the property value."""

        class TestClass:
            """Simple class exposing a memoized property."""

            def a_method(self):
                """Return a fixed value to assert memoization."""
                return 42

            @memoize
            def a_property(self):
                """Return memoized value by delegating to a_method."""
                return self.a_method()

        test_obj = TestClass()
        with patch.object(test_obj, "a_method") as mock_method:
            mock_method.return_value = 42
            self.assertEqual(test_obj.a_property, 42)
            mock_method.assert_called_once()
