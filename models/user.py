#!/usr/bin/python3
"""Import required libraries/modules"""
from hashlib import md5
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), unique=True)
    last_name = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(255), unique=True)
    phone = Column(Integer, unique=True)
    address = relationship("Address", backref="user")

    def __init__(self, *args, **kwargs):
        """Initialize the user"""
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """Returns the representation of the user"""
        return "User(first_name='%s', last_name='%s', email='%s', password='%s', phone='%s', address='%s')>".format(
            self.first_name, self.last_name, self.email, self.password, self.phone, self.password, self.phone,
            self.address)

    def __setattr__(self, name, value):
        """set a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
            super().__setattr__(name, value)
