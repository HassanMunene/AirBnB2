#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

#to show how many objects in the __objects dictionary
all_objs = storage.all()

print("--------RELOADED OBJECTS------")
print("--------from the file if there are any-------")
for key in all_objs.keys():
    obj = all_objs[key]
    print(obj)

print("\n-------CREATE A NEW OBJECT-------")
