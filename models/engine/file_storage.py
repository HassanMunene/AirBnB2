import os.path
import json
from models.base_model import BaseModel

class FileStorage():
    """
    This class will be used to serialize and deserialize instances of class a class to and from a JSON file
    it has 2 private class attributes __file_path and __objects which are both very essential to the functioning of the class
    __file_path is a string that represents where the serealized instance of a class will stored after being made a JSON string
    __objects attribute is decalared as an empty dictionary but will store the objects by their class name and ID.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This func is used to return the __objects dictionary so as to retrieve all the objects that have been created and stored in the __objects dictionary by default it is empty but as you create and save instances it will eventually be populated
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        this method will be used to add on object to the __objects dictionary
        with a key that consits of object's class name and its ID
        It takes object as the only argument and it used the objec's class name and id to create a key for the __objects dictionary
        You should always call this method after creating a new instance to ensure that it is stored in the __objects dictionary and later JSON file
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        this method serializes the __objects dictionary to the JSON file at the location specified by file-path
        You should always call the save() after adding or moifying the objects in the __objects dictionary
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
              obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
              json.dump(obj_dict, f)


    def reload(self):
        """
        This method is used to deserialize a JSON file at the file specified
        It then loads the objects into the __objects dictionary
        It first checks if the JSON file exists at the specified location by using the os.path.exists() function
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for k, v in data.items():
                    class_name = k.split(".")[0]
                    obj = eval(class_name)(**v)
                    FileStorage.__objects[k] = obj

