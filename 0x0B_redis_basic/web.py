#!/usr/bin/env python3
"""
This module provides a get_page function that fetches HTML content from a URL,
caches the result with a 10-second expiration, and tracks access counts.
"""
import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def count_url(method: Callable) -> Callable:
    """
    Decorator that tracks how many times a URL was accessed and caches
    the HTML content with a 10-second expiration.

    Args:
        method: The method to be decorated

    Returns:
        The wrapped method with caching and counting behavior
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper that handles counting and caching for the given URL."""
        r.incr("count:{}".format(url))

        cached = r.get("cached:{}".format(url))
        if cached:
            return cached.decode("utf-8")

        result = method(url)
        r.setex("cached:{}".format(url), 10, result)
        return result
    return wrapper


@count_url
def get_page(url: str) -> str:
    """
    Obtain the HTML content of a particular URL and return it.

    Args:
        url: The URL to fetch

    Returns:
        The HTML content of the URL
    """
    response = requests.get(url)
    return response.text
