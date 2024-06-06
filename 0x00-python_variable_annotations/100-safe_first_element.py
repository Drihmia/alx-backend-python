#!/usr/bin/env python3
"""This module contains safe_first_element as  function"""
from typing import Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Any:
    """safe_first_element"""
    if lst:
        return lst[0]
    else:
        return None
