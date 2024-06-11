#!/usr/bin/env python3
"""This module contains async_generator as asynchronous generator"""
import random
import asyncio
from typing import Generator


# An alternative: AsyncIterator[float] instead of AsyncGenerator[float, None]
async def async_generator() -> Generator[float, None, None]:
    """
    A coroutine that takes no arguments,
    will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
