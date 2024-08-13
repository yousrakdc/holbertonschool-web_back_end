#!/usr/bin/env python3
"""
Takes a list of strings and returns a list of tuples where each tuple
contains a string from the input list and its length
"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]
