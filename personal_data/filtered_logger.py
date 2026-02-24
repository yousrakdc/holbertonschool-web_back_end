#!/usr/bin/env python3
"""Module for filtering sensitive data from log messages."""

import os
import re
import logging
from typing import List, Tuple

import mysql.connector
from mysql.connector.connection import MySQLConnection


# Fields from user_data.csv considered as important PII.
# user_data.csv fields:
# name, email, phone, ssn, password, ip, last_login, user_agent
PII_FIELDS: Tuple[str, ...] = ("email", "phone", "ssn", "password", "name")


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """Return a log message with specified fields obfuscated.

    Args:
        fields: A list of field names whose values should be redacted.
        redaction: The string to replace field values with.
        message: The log line to process.
        separator: The character separating fields in the log line.

    Returns:
        The log message with sensitive field values replaced by
        the redaction string.

    Example:
        >>> filter_datum(["password"], "***", "user=John;password=s;", ";")
        'user=John;password=***;'
    """
    pattern = f'({"|".join(fields)})=([^{separator}]*)'
    return re.sub(pattern, lambda m: f'{m.group(1)}={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class that obfuscates sensitive fields."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with a list of fields to redact.

        Args:
            fields: A list of field names whose values will be
                obfuscated in logs.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format a log record, redacting sensitive field values.

        Args:
            record: The log record to format.

        Returns:
            The formatted log string with sensitive fields obfuscated.
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION,
            record.getMessage(), self.SEPARATOR
        )
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """Create and return a logger configured to redact PII fields.

    The logger is named 'user_data', logs up to INFO level only,
    does not propagate to parent loggers, and uses a
    RedactingFormatter on its StreamHandler to obfuscate PII_FIELDS.

    Returns:
        A configured logging.Logger instance.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=list(PII_FIELDS)))
    logger.addHandler(handler)

    return logger


def get_db() -> MySQLConnection:
    """Return a connector to the holberton MySQL database.

    Reads database credentials from the following environment variables:
        PERSONAL_DATA_DB_USERNAME (default: "root")
        PERSONAL_DATA_DB_PASSWORD (default: "")
        PERSONAL_DATA_DB_HOST     (default: "localhost")
        PERSONAL_DATA_DB_NAME

    Returns:
        A MySQLConnection object connected to the target database.
        The caller is responsible for closing the connection by calling
        .close() on the returned object when it is no longer needed.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )
