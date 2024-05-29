#!/usr/bin/python3
"""Import required libraries/modules"""
from sqlalchemy import Column, String, Integer

import models
from models.base_model import BaseModel, Base


class Images(BaseModel, Base):
    """Represents Images properties"""
    __tablename__ = 'images'
    image_id = Column(Integer, primary_key=True)
    original_filename = Column(String(255), nullable=False)
    upload_date = Column(nullable=False)
    original_size = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    color_space = Column(String(255), nullable=False)

    if models.storage_t != "db":
        pass

    def __init__(self, *args, **kwargs):
        """Initialize Images"""
        super().__init__(*args, **kwargs)
