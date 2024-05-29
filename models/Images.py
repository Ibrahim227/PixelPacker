#!/usr/bin/python3
"""Import required libraries/modules"""
from sqlalchemy import Column, String, Integer, DateTime

import models
from models.base_model import BaseModel, Base


class Images(BaseModel, Base):
    """Represents Images properties"""
    if models.storage_t == 'db':
        __tablename__ = 'images'
        image_id = Column(Integer, primary_key=True)
        original_filename = Column(String(255), nullable=False)
        upload_date = Column(DateTime, nullable=False)
        original_size = Column(Integer, nullable=False)
        width = Column(Integer, nullable=False)
        height = Column(Integer, nullable=False)
        color_space = Column(String(255), nullable=False)
    else:
        image_id = ""
        original_filename = ""
        upload_date = ""
        original_size = ""
        color_space = ""

    def __init__(self, *args, **kwargs):
        """Initialize Images"""
        super().__init__(*args, **kwargs)
