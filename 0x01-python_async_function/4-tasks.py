#!/usr/bin/env python3
"""This script takes an int and wait for random delay"""
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """"Returns a random delay"""
    tasks = [task_wait_random(task_id, max_delay) for task_id in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
