#!/usr/bin/env python3
"""Module"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """tuple containing the string k and the square of int/float v."""
    return (k, v ** 2)
