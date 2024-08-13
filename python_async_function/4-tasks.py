#!/usr/bin/env python3
"""
Creates `n` tasks using task_wait_random with the specified max_delay
returns a list of all delays in ascending order
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ returns a list of delays in ascending order."""
    async def gather_delays() -> List[float]:
        tasks = [wait_random(max_delay) for _ in range(n)]
        delays = await asyncio.gather(*tasks)
        return sorted(delays)
    return asyncio.run(gather_delays())
