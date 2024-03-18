#!/usr/bin/env python3
"""Module"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Import wait_random from the previous python file"""
    ran_delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(ran_delays)
