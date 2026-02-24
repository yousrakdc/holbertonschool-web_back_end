#!/usr/bin/env python3
"""
Module for filtering and obfuscating log messages containing PII
"""
import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message obfuscated by replacing specified field values
    with a redaction string.

    Args:
        fields: list of strings representing fields to obfuscate
        redaction: string to replace field values with
        message: string representing the log line
        separator: character separating fields in the log line

    Returns:
        The obfuscated log message
    """
    for field in fields:
        message = re.sub(
            f'{field}=.*?{separator}',
            f'{field}={redaction}{separator}',
            message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record and obfuscate the message
        """
        message = record.getMessage()
        record.msg = filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Get a logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a connector to the MySQL database using credentials from
    environment variables.

    Environment variables:
        PERSONAL_DATA_DB_USERNAME: database username (default: "root")
        PERSONAL_DATA_DB_PASSWORD: database password (default: "")
        PERSONAL_DATA_DB_HOST: database host (default: "localhost")
        PERSONAL_DATA_DB_NAME: database name

    Returns:
        MySQLConnection object
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )


def main():
    """
    Main function to demonstrate retrieving and displaying user data
    from the database with PII fields obfuscated.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    header = []
    for col in cursor.description:
        header.append(col[0])

    logger = get_logger()

    for row in cursor:
        info_message = ''
        for i, col in enumerate(row):
            info_message += f'{header[i]}={col};'
        logger.info(info_message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
