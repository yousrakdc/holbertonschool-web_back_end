#!/usr/bin/env python3
"""
Spawns `wait_random` `n` times with the specified `max_delay` and returns
a list of all delays in ascending order
"""


import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return list of delays"""
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    for result in results:
        delays.append(result)
        delays.sort()

    return delays
