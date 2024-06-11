#!/usr/bin/env python3
"""This module contains async_generator as asynchronous generator"""
from random import uniform
from asyncio import sleep
from typing import AsyncGenerator, Any


async def async_generator() -> AsyncGenerator[float, Any]:
    """
    A coroutine that takes no arguments,
    will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
