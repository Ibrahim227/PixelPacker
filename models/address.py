#!/usr/bin/python3
"""Import required libraries/modules"""
from sqlalchemy import Column, String, Integer, ForeignKey

from models.base_model import BaseModel, Base


class Address(BaseModel, Base):
    """Represents an address of a user"""
    if models.storage_t == 'db':
        __tablename__ = 'address'
        street_id = Column(Integer, primary_key=True, autoincrement=True)
        user_id = Column(Integer, ForeignKey('user.id'))
        street = Column(Integer, nullable=False)
        city = Column(String(255), nullable=False)
        state = Column(String(255), nullable=False)
        postal_code = Column(Integer, nullable=False)
        user = relationship("User", back_populates="address")
    else:
        street_id = ""
        street = ""
        city = ""
        state = ""
        postal_code = ""

    def __init__(self, *args, **kwargs):
        """Initialize the Address"""
        super().__init__(*args, **kwargs)
