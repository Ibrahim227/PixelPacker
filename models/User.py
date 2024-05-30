#!/usr/bin/python3
"""Import required libraries/modules"""
from hashlib import md5
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

import models


class User(BaseModel, Base):
    """Represents a user"""
    if models.storage_t == 'db':
        __tablename__ = 'user'
        id = Column(Integer, primary_key=True, auto_increment=True)
        first_name = Column(String(255), unique=True)
        last_name = Column(String(255), unique=True)
        email = Column(String(255), unique=False)
        password = Column(String(255), unique=False)
        phone = Column(Integer, unique=False)
        address = relationship("Address", backref="user")
    else:
        password = ""
        email = ""
        last_name = ""
        first_name = ""
        phone = ""

    def __init__(self, *args, **kwargs):
        """Initialize the user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """set a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
            super().__setattr__(name, value)
