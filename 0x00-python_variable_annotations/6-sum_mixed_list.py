#!/usr/bin/env python3
"""This scripts takes a list of flaot and it and return thier sum as float"""
from typing import List, Union

mixed_list = List[Union[int, float]]


def sum_mixed_list(mxd_lst: mixed_list) -> float:
    """Returns the sum of a mixed list as float"""
    sum = 0
    for num in mxd_lst:
        sum += num
    return sum
