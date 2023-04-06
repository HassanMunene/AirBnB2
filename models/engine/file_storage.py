#!/usr/bin/python3
"""
This contains a class whose work is to
serialize instance to a JSON file
deserializes JSON file to an instance
it contains two private class attributes
 - __file_path: this will contain a string which is the path to json file
 - __objects: it is a dictionary that will store objects
"""
import json


class FileStorage:
    """
    The class to do the dirty work of
    working with files
    """
    _file_path = "file_storage.json"
    _objects = {}

    def all(self):
        """
        this will return a dictionary
        consisiting of objects
        it will return __objects dictionary
        """
        return self._objects

    def new(self, obj):
        """
        adds an object to the obj dictionary
        with key <obj class name>.id
        first we need to get the name of the class the obj belongs
        Then we get the id of the id of the obj
        The use the two to form a key for the obj in dictionary
        Then assign the obj itself to the key
        """
        key = type(obj).__name__ + "." + obj.id
        self._objects[key] = obj

    def save(self):
        """
        This will serialize the objects in the __objects dict
        to Json string in the file provided in __file_path
        first of all the __objects dictionary cannnot be serialized
        this is because it contains some object that json do not accept
        therefore we need to first of all convert this __objects to a
        form that can be easily accepted that is using the to_dict() method
        The follwing is the structure of the _objects:
           -  key: obj
        what we need to use is the obj and not the key
        we will therefore the key in the process and select the values
        """
        serializable_dict = {}
        for obj in self._objects.values():
            serializable_dict = obj.to_dict()
        with open(self._file_path, mode='w', encoding='utf-8') as f:
            json_string = json.dumps(serializable_dict)
            f.write(json_string)
    def reload(self):
        """
        will be used to covert json file containnig
        json string to __objects only if the file file
        actually exists
        if it does not exist do nothing
        """
        try:
            with open(self._file_path, mode='r', encoding='utf-8') as f:
                json_string = f.read()
                if json_string:
                    self._objects = json.loads(json_string)
        except FileNotFoundError:
            pass

