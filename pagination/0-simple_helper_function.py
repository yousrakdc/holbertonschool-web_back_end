#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page & page_size
"""


def index_range(page, page_size):
    """A tuple (start_index, end_index)"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
