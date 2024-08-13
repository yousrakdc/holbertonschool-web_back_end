#!/usr/bin/env python3
"""
Takes a string and a numeric value (integer or float), squares the numeric
value, converts it to float, and returns a tuple with the string and the
squared float value.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v ** 2))
