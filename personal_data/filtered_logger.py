#!/usr/bin/env python3
"""This module provides functionality to
filter sensitive data from log messages."""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Return a log message with specified fields obfuscated.

    Args:
        fields: A list of field names whose values should be redacted.
        redaction: The string to replace field values with.
        message: The log line to process.
        separator: The character separating fields in the log line.

    Returns:
        The log message with sensitive field values
        replaced by the redaction string.

    Example:
        >>> filter_datum(["password"], "***",
        "user=John;password=secret;", ";")
        'user=John;password=***;'
    """
    pattern = f'({"|".join(fields)})=([^{separator}]*)'
    return re.sub(pattern, lambda m: f'{m.group(1)}={redaction}', message)
