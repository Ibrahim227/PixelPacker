#!/usr/bin/python3
from sqlalchemy import Column, String, Integer, Text

from models.base_model import BaseModel, Base
import models


class CompressionParameters(BaseModel, Base):
    """Compression parameters"""
    if models.storage_t == 'db':
        __tablename__ = "compressionparameters"
        compression_id = Column(Integer, primary_key=True)
        image_id = Column(Integer)
        algorithm = Column(String(255), nullable=False)
        compression_level = Column(Integer, nullable=False)
        quantization_matrix = Column(Text, nullable=False)
        transform_method = Column(String(255), nullable=False)
    else:
        compression_id = ""
        image_id = ""
        algorithm = ""
        compression_level = ""
        quantization_matrix = ""
        transform_method = ""

    def __init__(self, *args, **kwargs):
        """Initialize CompressionParameters"""
        super().__init__(*args, **kwargs)
