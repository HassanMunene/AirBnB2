#!/usr/bin/python3
import sys
sys.path.append("..")

from base_model import BaseModel
from file_storage import FileStorage

object_1 = BaseModel()
object_1.name = "Hassan"
object_1.number = 14347
print("\nWe have instanitated an object using the BaseModel class\n")
print(object_1)
print("\n")
storage = FileStorage()
print("So far our FileStorage __objects dictionary is empty")
storage.all()
print("\nLet's add an object to the dictionary")


