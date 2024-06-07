#!/usr/bin/env python3
"""This module contains: to_kv as a function."""
from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple, where:
        - The first element of the tuple is the string k.
        - The second element is the square of the int/float v,
            annotated as a float.
    """
    return (k, math.pow(v, 2))
