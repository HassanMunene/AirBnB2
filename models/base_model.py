#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid
from datetime import datetime
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, String, Integer, DateTime


if getenv("HBNB_TYPE_STORAGE") == "db":
    metadata = MetaData()
    Base = declarative_base()
    Base.metadata = metadata
else:
    Base = object

class BaseModel:
    """
    A base class for all hbnb models
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Instatntiates a new model
        and assign some common attributes automatically
        """
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        Updates updated_at with current time when instance is changed
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Convert instance into dict format
        """
        new_dict = self.__dict__.copy()
        new_dict.pop('_sa_instance_state', None)
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        if "created_at" in new_dict:
            new_dict['created_at'] = new_dict['created_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')
        if 'updated_at' in new_dict:
            new_dict['updated_at'] = new_dict['updated_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')

        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def delete(self):
        """
        delete current instance from the storage
        """
        models.storage.delete(self)
