#!/usr/bin/python3
"""Import required libraries/modules"""
from sqlalchemy import Column, String, Integer, ForeignKey

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Address(BaseModel, Base):
    """Represents an address of a user"""
    __tablename__ = 'address'
    street_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    street = Column(Integer, nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    postal_code = Column(Integer, nullable=False)
    user = relationship("User", back_populates="address")

    def __init__(self, *args, **kwargs):
        """Initialize the Address"""
        super().__init__(*args, **kwargs)
