#!/usr/bin/env python3
"""This script takes a list of floating numbers and return their sum"""


lists = list[float]
def sum_list(input_list: lists) -> float:
    """Accepts a list of floats and return their sum as float"""
    sum = 0
    for num in input_list:
        sum += num
    return sum
