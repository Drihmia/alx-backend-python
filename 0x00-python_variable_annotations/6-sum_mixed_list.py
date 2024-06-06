#!/usr/bin/env python3
"""This module contains a function called sum_mixed_list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of list as float"""
    return sum(mxd_lst)
