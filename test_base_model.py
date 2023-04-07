#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My fist model"
my_model.my_number = 89
print(my_model)
my_model.save()
print("\n\n")
print(my_model)
my_model_dict = my_model.to_dict()
print("\n\n")
print(my_model_dict)
print("\n")
print("JSON of my_model")
for key in my_model_dict.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_dict[key]), my_model_dict[key]))
