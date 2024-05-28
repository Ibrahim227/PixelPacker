import models
from os import getenv
from models.base_model import Base
from models.User import User
from models.Images import Images
from models.Address import Address
from models.CompressedImages import CompressedImages
from models.CompressionParameters import CompressionParameters
import sqlalchemy
from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
    "User": User,
    "Images": Images,
    "Address": Address,
    "CompressedImages": CompressedImages,
    "CompressionParameters": CompressionParameters
}


class DBStorage:
    """interact with the MySQL db"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate the DBStorage object"""
        PIXELPACKER_MYSQL_USER = getenv('PIXELPACKER_MYSQL_USER')
        PIXELPACKER_MYSQL_PWD = getenv('PIXELPACKER_MYSQL_PWD')
        PIXELPACKER_MYSQL_HOST = getenv('PIXELPACKER_MYSQL_HOST')
        PIXELPACKER_MYSQL_DB = getenv('PIXELPACKER_MYSQL_DB')
        PIXELPACKER_ENV = getenv('PIXELPACKER_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(PIXELPACKER_MYSQL_USER, PIXELPACKER_MYSQL_PWD,
                                                 PIXELPACKER_MYSQL_HOST, PIXELPACKER_MYSQL_DB))
        if PIXELPACKER_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on current db"""
        new_dict = {}
        for k in classes:
            pass
