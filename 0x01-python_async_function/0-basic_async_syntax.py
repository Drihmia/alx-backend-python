#!/usr/bin/env python3
"""Module that contains a async function called wait_random"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that takes in an integer argument (max_delay,
    with a default value of 10) named wait_random that waits for a random delay
    between 0 and max_delay (included and float value) seconds and eventually
    returns it.
    """

    rand: float = random.uniform(0, max_delay)
    # print(f"starts with {max_delay} with the value waited {rand}")
    await asyncio.sleep(rand)
    # print(f"ends with {max_delay} with the value waited {rand}")
    return rand
