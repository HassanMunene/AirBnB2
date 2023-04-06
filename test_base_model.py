#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My fist model"
my_model.my_number = 89
print(str(my_model))
my_model.save()
print("\n\n")
print(my_model)
my_model_json = my_model.to_dict()
print("\n\n")
print(my_model_json)
print("\n")
print("JSON of my_model")
for key in my_model_json:
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))