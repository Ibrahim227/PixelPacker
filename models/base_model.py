from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid


time = "%Y-%m-%dT%H:%M:%S.%f"
if models.storage_t == "db":
    Base = declarative_base()
else:
    Bae = object


class BaseModel:
    """Main class for all models"""
