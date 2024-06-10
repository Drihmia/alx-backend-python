#!/usr/bin/env python3
"""Module that contains a async function called wait_random"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that  that takes in 2 int arguments (in this order):
    n and max_delay. You will spawn wait_random n times with the
    specified max_delay.

    Return: a list of all the delays (float values). The list of the delays
    should be in ascending order without using sort() because of concurrency.
    """

    list_wait_random = [wait_random(max_delay) for _ in range(n)]

    # task_as_completed = []
    # for task in asyncio.as_completed(list_wait_random):
    # result = await task
    # task_as_completed.append(result)
    # return task_as_completed
    return [await t for t in asyncio.as_completed(list_wait_random)]
