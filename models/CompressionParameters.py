#!/usr/bin/python3
from sqlalchemy import Column, String, Integer, Text, ForeignKey

import models
from models.base_model import BaseModel, Base


class CompressionParameters(BaseModel, Base):
    """Compression parameters"""
    __tablename__ = "compressionparameters"
    compression_id = Column(Integer, primary_key=True)
    image_id = Column(Integer)
    algorithm = Column(String(255), nullable=False)
    compression_level = Column(Integer, nullable=False)
    quantization_matrix = Column(Text, nullable=False)
    transform_method = Column(String(255), nullable=False)

