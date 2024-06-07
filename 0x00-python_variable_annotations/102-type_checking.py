#!/usr/bin/env python3
"""This module contains zoom_array as a function"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a zoomed list of lst by the factor"""
    zoomed_in: List = [
        item for item in lst
    ]
    return zoomed_in * factor


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
