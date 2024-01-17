#!/usr/bin/python3
"""This module defines a class User"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(
            string(128), nullable=False
            )
    password = Column(
            string(128), nullable=False
            )
    first_name = Column(
            string(128), nullable=False
            )
    last_name = Column(
            string(128), nullable=False
            )
    places = relationship(
            'Place',
            cascade="all, delete, delete-orphan",
            backref='user'
            )
    reviews = relationship(
            'Review',
            cascade="all, delete, delete-orphan",
            backref='user'
            )
