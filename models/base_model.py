#!/usr/bin/python3
"""
The mother of all classes that will be
We will use the this class as a base when declaring
other classes in the project
it contains all the common attributes that
all other classes will have
This class will serve as a parent to all other classes.
By inheriting from the BaseModel other classes can take advantage of 
the attributes and methods in this class without really having to redefine them.
This will promote code re-usability, maintainability and consistency across different classes
This class contains the following attribute:
    - id: this is a string that will hold a unique identifier for each instance of BaseModel or derived class
    - created_at: a datetime attribute that will hold the timestamp of when an instance of BaseModel or derived class was created.
    - updated_at: datetime attribute that holds the timestamp of the most recent update to an instance of BasemModel or derived class.
        It can be updated automatically when the save method is called
    - save(self): will be used to update the updated_at time.
                this method will be used after modifiying the instance
    - to_dict(self): This method will return a dictionary representation of the instance of BaseModel or derived class.
                    This dictionary will include all the instance attributes
                    This method is useful for serializing instances of the class for storage or transmission
"""
import uuid
import datetime
import storage


class BaseModel:
    """
    The base class that all other
    classes will inherit from
    """

    def __init__(self, *args, **kwargs):
        """
        attributes automatically instatited when an object is
        created
        This method takes the following arguments:
            *args: This will not be utilized
            **kwargs: if this is not empty then it means we are passing a dictionary.
                    That dictionary needs to be passed backed to an instance of the class
                    On the other hand created_at and updated_at attributes
                    in the dictionary are strings but they need to be coverted back to datetime objects
                    If the kwargs is empty then it means we are creating a new instace.
        """
        if kwargs:
            for key in kwargs.keys():
                if key != '__class__':
                    self.created_at = datetime.datetime.now()
                    self.updated_at = datetime.datetime.now()
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            storage.new()

    def __str__(self):
        """
        returns a string representation of the object
        in a readable format
        This string will contain the following to object at the beginning
         - the name of the class the object belongs ti
         - the id of the object
         - after this we will use __dict__ attribute to print the rest
        """
        return "[{}] ({}) <{}>".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        When called it updates the updated_at attribute
        with the current time
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        this method will return a dictionary representation of
        the object and in that dictionary we will also include the
        class name of the object and its key will be __class__
        """

        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        for key in self.__dict__.keys():
            new_dict[key] = self.__dict__[key]
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.created_at.isoformat()
        return new_dict
