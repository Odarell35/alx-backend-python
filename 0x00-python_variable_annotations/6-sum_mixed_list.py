#!/usr/bin/env python3
"""Module"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of integers and floats in a mixed list."""
    return sum(mxd_lst)
