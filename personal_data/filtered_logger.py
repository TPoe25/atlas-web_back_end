#!/usr/bin/env python3
"""
This module provides a logger that redacts sensitive PII data,
and a secure method to connect to a MySQL database using environment variables.
"""

import logging
import re
import os
import mysql.connector
from mysql.connector import MySQLConnection, Error
from typing import List, Tuple, Optional

# Define PII fields that should be redacted in logs
PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): Fields to obfuscate.
        redaction (str): The string to replace field values with.
        message (str): The log message containing data.
        separator (str): The field separator.

    Returns:
        str: The obfuscated log message.
    """
    pattern = r'(' + '|'.join(fields) + r')=[^' + separator + r']*'
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for logging, filtering out PII data.

    Attributes:
        REDACTION (str): The string used to replace sensitive information.
        FORMAT (str): The format string for log messages.
        SEPARATOR (str): The separator used to split log messages into fields.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter with fields to redact.

        Args:
            fields (List[str]): The list of field names to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format a log record, redacting sensitive fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted and redacted log message.
        """
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger named 'user_data'.

    - Logs only up to logging.INFO level.
    - Does not propagate messages to other loggers.
    - Uses a StreamHandler with RedactingFormatter to filter PII.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def get_db() -> Optional[MySQLConnection]:
    """
    Return a connector to the MySQL database using environment variables.

    Returns:
        MySQLConnection | None: The database connection, or None on failure.
    """
    try:
        # Fetch credentials from environment variables
        username: str = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
        password: str = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
        host: str = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
        db_name: Optional[str] = os.getenv('PERSONAL_DATA_DB_NAME')

        if not db_name:
            raise ValueError("Environment variable PERSONAL_DATA_DB_NAME is required")

        # Establish the connection
        connection: MySQLConnection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=db_name
        )

        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        return None


# Optional testing block
if __name__ == "__main__":
    # Test connection and logger output (can be removed or customized)
    logger = get_logger()
    logger.info("name=John Doe; email=john@example.com; ssn=123-45-6789;")

    db = get_db()
    if db:
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM users;")
        for row in cursor:
            print(f"User count: {row[0]}")
        cursor.close()
        db.close()
