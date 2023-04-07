#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objects = storage.all()

print("---------RELOADED OBJECTS-----------")
for key in all_objects.keys():
    obj = all_objects[key]
    print(obj)

print("\n")
print("--------CREATE A NEW OBJECT---------")
my_model = BaseModel()
my_model.name = "My_first_model"
my_model.my_number = 89
my_model.save()
print(my_model)

