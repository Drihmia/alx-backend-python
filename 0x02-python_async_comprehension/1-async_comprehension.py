#!/usr/bin/env python3
"""This module contains async_comprehension as coroutine"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine That takes no arguments.

    The coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    return [task async for task in async_generator()]
