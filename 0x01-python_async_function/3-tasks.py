#!/usr/bin/env python3
"""Module"""


import asyncio
from typing import Callable
from asyncio import Task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """task_wait_random that takes an integer max_delay"""
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
