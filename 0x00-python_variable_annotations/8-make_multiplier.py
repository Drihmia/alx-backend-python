#!/usr/bin/env python3
"""This module contains make_multiplier as a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return  a function that multiplies a float by multiplier."""
    def multiplier_fun(float_num):
        """
        Return the resutls of multiplication of the float_numand
            the and multiplier.
        """
        return multiplier * float_num
    return multiplier_fun
