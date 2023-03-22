## The __init__ part

The first part is a constructor method of python that us the __init__() method. This method is always called whenever an instance of the class is created.

In our case it will be used to set up some variables for the object being created.

The first line which is *self.id* is used to create a unique identifier for the object being created by giving it a UUID4 which is a random number.

The second and the third line are both related to date and time and they basically give the object a timestamp of when it was created and when it was updated.

so every object that is created from BaseModel will have these three attributes to describe it.

## The def __str__ part

This is the part of the code that returns the string represenation of the object that will be instatiated. This special method is important because it will help us print the object in  human readable form.

In our the __str__ method will return the following to us:
1. The name of the class from which our object has been instatiated
```
type(self).__name
```
1. The unique uuid of the object
```
self.id
```
1. The dictionary of the object being created i.e the attributes and the values of the object
```
self.__dict__
```

## The save part
This is the method that enables us to keep tract of when the object was uupdated or when the object was manipulated

When this method is called by the object it automaticalyy update the time to indicate when an object was updatd

## The to_dict part.

Now this is the section of the code that returns the dictionary representation of the object. This method takes in a copy of the object dictionary and then adds to it a key-value pair of *__class__* and the name of the class. it was adjusts the created_at and updated_at date and time to an ISO formatted string

## SO WHAT THE PURPOSE
The puprpose of to_dict is to provide a way to serialize the object created into a format that can be easily saved and transmitted such JSON nad YAML. By converting the object to a dictionary then it can easily be conveted to A JSON string using python built in fucntions
