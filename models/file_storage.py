#!/usr/bin/python3
"""
This module is about creating a class called FileStorage
This class will be used to store and retrieve all the instances of
classes created in this project
They will be stored in form of a json string.
It will do the serialization and deserialization of the instances
To acheive this the class will have two private attributes:
    - __file_path: will store the path to the json file
    - __objects: will store the objects we want to save to the json file
The class too has some methods:
    - all(self): the function of this is to return the __objects
    - new(self, obj): add an object to the dictionary __objects
    - save(self): After adding the object this func will serealize all the objects in the __objects dictionary
        and save the string to the file specified
    - reload(self): this will read the string in the file and then to __objects on if the file exists

After creating the class then the next step is to make it available
to all the classes created in the project
This is made possible by creating an instance of the class in the __init__.py file
We will then call the reload() method of the class because we want to load any existing data

From the json file into memory when the application starts up.
If we do not call the reload() the __objects dictionary in the instance will be empty and any prevoiusly saved data will be lost

This is extremely important for applications that need to maintain
state between sessions or across multiple instances of the application
"""


class FileStorage:
    """
    The class itself
    __objects is a dictionary and will store all the instnaces of the
        classes that need to be saved.
        The key of __objects will be as follows:
            <class name>.instance id
    """

    __file_path = "file.json"
    __objects = {}
