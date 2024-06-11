#!/usr/bin/env python3
"""This module contains measure_runtime as coroutine"""
from time import perf_counter
from asyncio import gather, create_task
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    A coroutine that will execute async_comprehension four times in parallel
    using asyncio.gather.
    """
    start = perf_counter()

    # tasks = []
    # for _ in range(4):
    # tasks.append(create_task(async_comprehension()))
    # await gather(*([task for task in tasks]))

    await gather(*(create_task(async_comprehension()) for _ in range(4)))
    end = perf_counter()

    return end - start
