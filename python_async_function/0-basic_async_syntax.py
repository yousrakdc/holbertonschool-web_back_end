#!/usr/bin/env python3
"""
Asynchronously waits for a random delay between 0 and max_delay seconds
and returns the delay
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Generate a random float between 0 and max_delay"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
