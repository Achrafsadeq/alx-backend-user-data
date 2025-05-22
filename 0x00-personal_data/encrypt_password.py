#!/usr/bin/env python3
"""
Module for encrypting and validating passwords using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with salt.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against its hashed version.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
