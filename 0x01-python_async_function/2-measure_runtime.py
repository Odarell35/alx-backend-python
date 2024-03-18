#!/usr/bin/env python3
"""Module"""


from typing import Callable
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time function with integers n and max_delay"""
    initial = time.time()
    asyncio.run(wait_n(n, max_delay))
    final = time.time()
    total_time = final - initial
    return total_time / n
