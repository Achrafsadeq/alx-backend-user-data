#!/usr/bin/env python3
"""
User model module for the authentication service.
This module contains the SQLAlchemy User model for database operations.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User model class for the authentication database.

    This class represents a user in the authentication system with
    all necessary fields for user management and session handling.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
