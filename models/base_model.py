#!/usr/bin/python3
"""
The mother of all classes that will be
instantiated thereafter
it contains all the common attributes that
all other classes will have
"""
import uuid
import datetime


class BaseModel:
    """
    The base class that all other
    classes will inherit from
    """

    def __init__(self):
        """
        attributes instatited when an object is
        created
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def __str__(self):
        """
        returns a string representation of the object
        in a readable format
        """
        return "[{}] ({}) <{}>".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        When called it updates the updated_at attribute
        with the current time
        """
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """
        this method will return a dictionary representation of
        the object and in that dictionary we will also include the
        class name of the object and its key will be __class__
        """

        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        for key in self.__dict__:
            new_dict[key] = self.__dict__[key]
        return new_dict
