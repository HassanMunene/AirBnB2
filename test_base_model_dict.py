#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_second_model"
my_model.number = 89
print("This is the id that an instance is give")
print(my_model.id)
print("\n\n")
print("The string representation of the object __str__\n")
print(my_model)
print()
print(type(my_model.created_at))
print("-----------------------------------------")
print("-----------------------------------------")
print("Convert the object to a dictionary representation")
my_model_dict = my_model.to_dict()
print(my_model_dict)
print()
"""print("JSON of my model")
for key in my_model_json:
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
print()
print("------------PASSING KWARGS TO THE MODEL-------------")
my_new_model  = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))
print("-----------------")
print(my_model is my_new_model)"""
