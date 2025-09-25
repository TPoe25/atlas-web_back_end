#!/usr/bin/env python3
"""
encrypt_password module
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a generated salt.

    Args:
        password (str): The plain-text password.

    Returns:
        bytes: The salted, hashed password.
    """
    password_bytes = password.encode('utf-8')  # convert to bytes
    salt = bcrypt.gensalt()  # generate a new salt
    hashed = bcrypt.hashpw(password_bytes, salt)  # hash the password
    return hashed

def is_valid(hashed_password: bytes, password: str) -> bool:
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)
