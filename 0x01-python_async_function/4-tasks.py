#!/usr/bin/env python3
'''Module contains task_wait_n as a function'''
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n, may_delay):
    """A function that alter  from wait_n function"""
    task = await asyncio.create_task(wait_n(n, may_delay))
    return task
