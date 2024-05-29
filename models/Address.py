#!/usr/bin/python3
"""Import required libraries/modules"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy import relationship

import models


class Address(BaseModel, Base):
    """Represents an address of a user"""
    __tablename__ = 'address'
    street_id = Column(Integer, primary_key=True)
    street = Column(Integer, nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    postal_code = Column(Integer, nullable=False)
