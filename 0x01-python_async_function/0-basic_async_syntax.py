#!/usr/bin/env python3
"""
first use of async function(async def ...)
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    write an asynchrinous coroutine that takes
    in an integer argument max_delay with value of 10
    (max_delay: int = 10) that waits for a rondom delay between
    0 and max_delay include and float value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
