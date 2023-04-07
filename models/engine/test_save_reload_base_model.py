#!/usr/bin/python3
import sys
sys.path.append("..")

from base_model import BaseModel
from file_storage import FileStorage

object_1 = BaseModel()
object_1.name = "Hassan"
object_1.number = 14347
print("\n")
storage = FileStorage()
print("So far our FileStorage __objects dictionary is empty")
storage.all()
print("\nLet's add an object to the dictionary\n")
storage.new(object_1)
storage.save()

print("\ncreating another object_2")
object_2 = BaseModel()
object_2.name = "Munene"
object_2.number = 2104609
print("\n")
storage = FileStorage()
print("So far our FileStorage __objects dictionary is having one objet")
storage.all()
print("\nLet's add an object to the dictionary\n")
storage.new(object_2)

print("\n\n Now we have two objects in the __objects dict lets serializae them to file.json")
storage.save()
print("\n\n\n")
storage.reload()
