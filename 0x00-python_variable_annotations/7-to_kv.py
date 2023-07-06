#!/usr/bin/env python3
"""This scripts takes a str and int or float and returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str,  v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string and int or float and returns a tuple"""
    variable: Tuple[str, float]
    variable = (k, v * v)
    return variable
