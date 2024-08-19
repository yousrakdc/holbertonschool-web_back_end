#!/usr/bin/env python3
'''
will execute async_comprehension four times in parallel using asyncio.gather
'''


import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure runtime"""
    start_time = time.default_timer()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.default_timer()
    total_time = end_time - start_time
    return total_time
