#!/usr/bin/python3
"""Import required libraries/modules"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, BLOB
from sqlalchemy import relationship

import models


class CompressedImages(BaseModel, Base):
    """Represents the Compressed image"""
    __tablename__ = 'compressedimages'
    compressed_images_id = Column(Integer, primary_key=True)
    image_id = Column(Integer, nullable=False)
    compressed_size = Column(Integer, nullable=False)
    compressed_ratio = Column(Float, nullable=False)
    compressed_filename = Column(String(255), nullable=False)
    compressed_data = Column(BLOB, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize CompressedImages"""
        super().__init__(*args, **kwargs)
