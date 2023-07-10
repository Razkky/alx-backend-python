#!/usr/bin/env python3
"""This scripts uses await fucntion to wait for random value"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for for random delay between 0 and max_delay and returns value"""
    delay_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time