#!/usr/bin/python3
"""
This module is about creating a class called FileStorage
This class will be used to store and retrieve all the instances of
classes created in this project
This class will make the objects created in a program persist
meaning that they will still exist even after the program has been
terminated or restarted
They will be stored in form of a json string which is the standard
way of representing data strucutures that can be easily read and written by humans and languages
It will do the serialization and deserialization of the instances
The following will be the flow of serialization and desearialization:
    - Convert object to dictionary
    - Convert dictionary to JSON string
    - Write the string to an file
    - Convert the string back to a dictionary
    - Create an object from the dictinary
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
import datetime
import json


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

    def all(self):
        """
        will return the dictionary __objects
        purpose: to show us the objects contianed in the __objects
        """
        print(self.__objects)
        return self.__objects
    
    def new(self, obj):
        """
        add an object to the __objects dictionary.
        The key of the object will be a combination of class name and id
        First we need to create the key for the object to be used.
        """

        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()
        print(self.__objects)

    def save(self):
        """
        take the objects in the __objects dictionary and serialize them
        Then store them to a file called file.json
        First of all the dictionary as it is now is not serializable.
        because it contains class BaseModel which cannot be serialized
        We will create a new dictionary that we will use to 
        """
        new_dict = {}
        for obj in self.__objects.values():
            pass
        new_dict = obj
        print(new_dict)
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json_string = json.dumps(new_dict)
            f.write(json_string)
