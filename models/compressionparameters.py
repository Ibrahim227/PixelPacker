#!/usr/bin/python3
from sqlalchemy import Column, String, Integer, Text

from models.base_model import BaseModel, Base
from models.images import Images


class CompressionParameters(BaseModel, Base):
    """Compression parameters"""
    __tablename__ = "compressionparameters"
    compression_id = Column(Integer, primary_key=True)
    image_id = Column(Integer)
    algorithm = Column(String(255), nullable=False)
    compression_level = Column(Integer, nullable=False)
    quantization_matrix = Column(Text, nullable=False)
    transform_method = Column(String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize CompressionParameters"""
        super().__init__(*args, **kwargs)
