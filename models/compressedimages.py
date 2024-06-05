#!/usr/bin/python3
"""Import required libraries/modules"""
from sqlalchemy import Column, String, Integer, Float, BLOB

import models
from models.base_model import BaseModel, Base


class CompressedImages(BaseModel, Base):
    """Represents the Compressed image"""
    if models.storage_t == 'db':
        __tablename__ = 'compressedimages'
        compressed_images_id = Column(Integer, primary_key=True)
        image_id = Column(Integer, nullable=False)
        compressed_size = Column(Integer, nullable=False)
        compressed_ratio = Column(Float, nullable=False)
        compressed_filename = Column(String(255), nullable=False)
        compressed_data = Column(BLOB, nullable=False)
    else:
        compressed_images_id = ""
        image_id = ""
        compressed_size = ""
        compressed_ratio = ""
        compressed_filename = ""
        compressed_data = ""

    def __init__(self, *args, **kwargs):
        """Initialize CompressedImages"""
        super().__init__(*args, **kwargs)
