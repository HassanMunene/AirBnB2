#!/usr/bin/python3
"""
The mother of all classes that will be
We will use the this class as a base when declaring
other classes in the project
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

    def __init__(self, *args, **kwargs):
        """
        attributes automatically instatited when an object is
        created
        """
        if kwargs:
            for key in kwargs:
                if key is not '__class__':
                    self.created_at = datetime.datetime.now()
                    self.updated_at = datetime.datetime.now()
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()

    def __str__(self):
        """
        returns a string representation of the object
        in a readable format
        This string will contain the following to object at the beginning
         - the name of the class the object belongs ti
         - the id of the object
         - after this we will use __dict__ attribute to print the rest
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        When called it updates the updated_at attribute
        with the current time
        """
        self.updated_at = datetime.datetime.now()

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
