#!/usr/bin/env python3
"""
This module contains a coroutine that generates random numbers asynchronously.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously generates 10 random numbers between 0 and 10.
    Each number is yielded after waiting for 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
