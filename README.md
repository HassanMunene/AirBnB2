![AirBnB](https://github.com/HassanMunene/AirBnB_clone/blob/main/images/AirBnB1.png)

The goal of this project is to deploy on my server a simple copy of the AirBnB website.

I won't implement all the features only some of them to cover all the fundamental concepts.

After the completion of this project I should have a complete web application composed by:
 - A command interpreter to manipulate data without a visual interface like a shell(perfect for development and debugging)
 - A website (front-end) that shows the final product to everybody: both static and dynamic
 - A database or files that store data(data = objects)
 - An API that provides a communication interface between the frontend and your data (retrieve, create, delete and update them CRUD)

## HOW THE FINAL PRODUCT SHOULD LOOK LIKE

![AirBnB-website](https://github.com/HassanMunene/AirBnB_clone/blob/main/images/airbnb1.png)


![Airbnb-website](https://github.com/HassanMunene/AirBnB_clone/blob/main/images/airbnb2.png)

## VIDEOS SHOWING HOW VARIOUS PARTS OF THE PROJECT WORK

![Watch Overview Video](https://www.youtube.com/watch?v=tFDUHXxZsYg)

![About The Console](https://www.youtube.com/watch?v=INn8YzN_YJM)

![ORM Object-Relational-Mapping](https://www.youtube.com/watch?v=ZwCD8cNZk9U&feature=youtu.be)

![RESTful API](https://www.youtube.com/watch?v=YiDX1rY8imw&feature=youtu.be)

![The final Product](https://www.youtube.com/watch?v=m-cfupVumos)

## CONCEPT TO LEARN IN THIS PROJECT

1. Unittest
1. Python packages
1. Serailization/Deserialization
1. **args, **kwargs
1. datetime

## THE CONSOLE
- Create your data model
- Manage (CRUD) objects via a console/command interpreter
- store and persist objects to a file (JSON FILE)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between "My Object" and "How they are stored and persisted"

From my console code and from the front-end and RestAPI that I will build later, I wont have to pay attention of how my objects are stored.

![Backend-Frontend-pic-overview](https://github.com/HassanMunene/AirBnB_clone/blob/main/images/webAppOverview.png)

## WEB STATIC
- learn HTML/CSS
- Create HTML of my application
- Create a template for each object

## MySQL storage
- Replace the file storage by a database storage
- map my models to a table in database by using an O.R.M

## WEB FRAMEWORK - templating
- Create my first web server in Python
- make my static HTML file dynamic by using object stored in a file or a database

## RESTful API
- Expose all my objects stored via a JSON web interface
- Load objects from client side by using my own RESTful API

# STORAGE
Persistent is very important in a web application. It means that everytime my program is executed, it start with all the objects prevoiusly created from another execution. Without percistent all the work done in a previous execution is not saved and will be gone.

In this project we will manipulate 2 types of storage:
1. File storage
1. Database storage

Why do we separate storage management from models. This is to make our models modular and independent. With this architecture we can easily replace our storage system without having recode everything everywhere.

## How To store my instances

Let's take a look at the code below.
```
class Student():
	def __init__(self, name):
		self.name = name

# create an empty list called students
students = []
 
# create an object of the Student class
s = Student("Hassan")

# add that instance to the student list. So in our list of students we have one student
student.append(s)
```

What we have done here is that we have created a student and stored it in a list. but after the execution my student instance is lost does not really exist anymore.

If we want to to save our student instance we have to add some more code as shown below

```
class Student():
	def __init__(self, name):
		self.name = name

students = []
s = Student("Hassan")
students.append(s)
# save all the students objects to a file
save(students)

```
## But The question Is How does This really even work??

let's first look at *save(students)* 
- can someone wite each Student object to a file? The answer is NOO!! This is because it will be a memory representation of the object amd for another program execution the memory representation cannot be reloaded.
- can we write Student.name to a file? YES!! BUT imagine a Student having more attributes to describe a student that would be a pain to write all those attributes. It would become really complex.

So the best solution is to convert the list of Student objects to a JSON representation.

## WHY JSON.
because it is the standard representation of objects. It allows us to share this data with other developers, it is human readable and also mainly to be understood by another language/program.

#### Example:
	- my python program creats a Student object and saves then to a JSON file
	- another Javascript program can read this JSON file and manipulate its own Student class/representation

## File storage == JSON Serialization

- write in a file all your objects/instances created/updated in your command and restore them when you start it.
- you cannot restore and store a python instance of a class as bytes the only way is to covert it to serializable data structure.
- covert an instance to python built in serializable data structure(list, dict, number and string) 
- convert this data structure to a string(JSON format but it can also be YAML, XML, CSV..) for us it will be *my_string = JSON.dumps(my_dict)*
- Write this string to a file on a disk

## JSON DESERIALIZATION

- Read s string from a file on disk
- convert this string to data-structure. This string is a JSON representation so it is easy to convert. *my_dict = JSON.loads(my_string)*
- convert this data structure to instance- *my_instance = MyObject(my_dict)

# \*args, \*\*kwargs

### How to pass arguments to a function
```
def my_func(param1, param2):
	pass

my_func("Best", "School")
```
The problem with this function is that you must call my_func with 2 parameters otherwise it will not work.
What if we want to make that function dynamic such that it can receive any number of parameters and still work, is it possible? YES !! it is very much.

```
def my_func(*\args, *\*\kwarg):
	pass

my_func("Best", "school")
or
my_func("Best", "school", "ever")

# they are both valid
```

So what is \*args and \*\*kwargs

\* args is a tuple that contains all the arguments 
\*\*kwargs is the dictionary with all the argguments by key/value

#### Example
```
def my_func( \*args, \*\*kwargs):
	print("{} - {}".format(args, kwargs))

my_func() # () - {}
my_func("best") # ('best',) - {}
my_func("best", 89) # ('best', 89) - {}
my_func(name="Best", number=89) # () - {'name': 'Best', 'number': 89}
my_func("school", 12, name="Best", number=89) # ('school', 12) - {'name': 'Best', 'number': 89}
```
## datetime

This is a python module to manipulate date and time

You can create an instance of datetime with the current date and time

```
from datetime import datetime

date_now = datetime.now()
print(type(date_now))  # <class 'datetime.datetime'>
print(date_now)  # 2023-03-21 13:35:22.748922
```
You can also store it. 

```
a_dict = {'my_date': date_now}
print(type(a_dict['my_date'])) # <class 'datetime.datetime'>
print(a_dict) #  {'my_date': datetime.datetime(2023, 3, 21, 13, 44, 9, 638064)}
```

