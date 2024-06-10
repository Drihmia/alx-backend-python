#!/usr/bin/env python3
'''Module contains task_wait_n as a function'''
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """A function that alter  from wait_n function"""
    task = await asyncio.create_task(wait_n(n, max_delay))
    return task
