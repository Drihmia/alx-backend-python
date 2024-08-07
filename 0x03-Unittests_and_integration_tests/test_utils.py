#!/usr/bin/env python3
"""
This module contains the unit tests for the utils module.
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from utils import memoize
import utils
from typing import Dict, List, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):  # noqa: N801
    """A test case for the access_nested_map method."""

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2),
                           ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: int) -> None:
        """A valid tests for access_nested_map"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """An invalid test for access_nested_map"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):  # noqa: N801
    """A test case for the get_json method."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get: Mock
                      ) -> None:
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


class TestMemoize(unittest.TestCase):  # noqa: N801
    """A test case for the memoize method."""

    def test_memoize(self) -> None:
        """A valid test case for the memoize method."""
        class TestClass:
            """ Testing class """

            def a_method(self) -> int:
                """A method that returns 42."""
                return 42

            @memoize
            def a_property(self) -> int:
                """A property that returns the result of a_method."""
                return self.a_method()

        test = TestClass()
        with patch.object(TestClass, 'a_method',
                          wraps=test.a_method) as mock_a_method:
            re_1 = test.a_property
            re_2 = test.a_property

            mock_a_method.assert_called_once()
            self.assertEqual(re_1, re_2)
