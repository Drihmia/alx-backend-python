#!/usr/bin/env python3
"""
This module contains the unit tests for the utils module.
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
import utils


class TestAccessNestedMap(unittest.TestCase):
    """A test case for the access_nested_map method."""

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2),
                           ])
    def test_access_nested_map(self, nested_map, path, expected):
        """A valid tests for access_nested_map"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A test case for the get_json method."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """A valid tests for get_json"""
        # Method 1: ---------------------------------------------
        response = Mock()
        response.json.return_value = test_payload
        mock_get.return_value = response
        # -------------------------------------------------------

        # Method 2: ---------------------------------------------
        # I've tried to mimic a mock object for learning purposes:
        # class mocking_mock:
        # def json(self):
        # return test_payload
        # object_with_json_method = mocking_mock()
        # mock_get.return_value = object_with_json_method
        # -------------------------------------------------------

        self.assertEqual(utils.get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """A test case for the memoize method."""

    @patch('test_utils.TestMemoize.TestClass.a_method')
    def test_memoize(self, mock_a_method):
        """A valid test case for the memoize method."""
        class TestClass:
            """ Testing class """

            def a_method(self):
                """A method that returns 42."""
                return 42

            @utils.memoize
            def a_property(self):
                """A property that returns the result of a_method."""
                return self.a_method()

        test = TestClass()
        test.a_property()

        mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
