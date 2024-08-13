#!/usr/bin/env python3
"""
Takes a list of strings and returns a list of tuples where each tuple
contains a string from the input list and its length
"""


from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return appropriate types"""
    return [(i, len(i)) for i in lst]
