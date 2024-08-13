#!/usr/bin/env python3
"""
Returns a function that multiplies a given float by the specified multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """'multiply' 'floats'"""
    return lambda n: (n * multiplier)
