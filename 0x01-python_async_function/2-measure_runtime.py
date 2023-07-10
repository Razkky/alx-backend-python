#!/usr/bin/env python3
"""This script measures execution time for wait_n function"""
import asyncio
import time
import random
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """Measures the execution time of wait_n function"""
    execution_time: float

    start = time.perf_counter()
    await wait_n(n, max_delay)
    execution_time = time.perf_counter() - start
    print("returning")
    return execution_time / n
