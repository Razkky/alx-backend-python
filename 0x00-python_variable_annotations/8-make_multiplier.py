#!/usr/bin/env python3
"""This script returns a function that multiplies a float by a multiplier"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a callable funciton"""
    def multiply(number: float) -> float:
        """Multiply the multiplier by number"""
        return multiplier * number
    return multiply