#!/usr/bin/python3
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.address import Address
from models.compressedimages import CompressedImages
from models.compressionparameters import CompressionParameters
from models.images import Images
from models.user import User
from models.base_model import Base

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
            if k is None or cls is classes[k] or cls is k:
                objs = self.__session.query(classes[k]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add it to the db session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to the db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """"delete obj to the db session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """"reload data from the db"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bin=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attr"""
        self.__session.remove()

    def get(self, cls, id):
        """returns the object"""
        all_cls = self.all(cls)
        for value in all_cls.values():
            if value.id == id:
                return value

        return None

    def count(self, cls=None):
        """Count the number of objects in storage"""
        all_classes = classes.values()

        if not cls:
            count = 0
            for cla in all_classes:
                count += len(self.all(cla).values())
        else:
            count = len(self.all(cls).values())

        return count
