## The flow of Serialization and deserialization

### <class 'Name of the class'> -> method() 'method the class to dictionary' -> <class 'dict'> JSON dump -> <class 'str'> -> FILE.json -> <class 'str'> JSON load -> <class 'dict'> -> <class 'name of the class'>

JSON is a format that encodes objects in a string. 

Serialization is converting an object into a string and deserialization is converting a string into an object

When transmitting data or string them in a file, the data is required to be byte strings, I have described what is a vyte string below.

### byte string:
This is just a sequence of bytes. it is not human readable. under the hood everything must be converted to a byte for it to be stored in a computer

so serialization converts complex objects into byte strings. After byte strings are transmitted, the receiver will have to recover the original object from the byte string. This is what is called deserialization.

say you have the following object:
```
{foo: [1, 4, 7, 10], bar: "baz"}
```
serealizing it into JSON will convert it into the folowing string
```
'{"foo":[1, 4, 7, 10], "bar":"baz"]'
```
This string can be stored and sent through wire to anywhere. The receiver will tthen deserialize the string back to the original object
```
{foo: [1, 4, 7, 10], bar: "baz"}

## JSON
So this is an open standard file format and data interchange format that uses human readable text to store and transmit data object. 

It is a common data format with diverse uses in electronic data interchange, including that of web application with servers.

It is a language independent data format. It was derived from javascript, but amny modern programming languages include code to generate and parse JSON-format data. .json(extension)

```
import json

data ={'president': {"name": """Mr. President""", "male": True, 'age': 60, 'wife': None, 'cars': ('BMW', "Audi")}}

# serealize

json_data = json.dumps(data, indent=2)

print(json_data)

{
  "president": {
    "name": "Mr. President",
    "male": true,
    "age": 60,
    "wife": null,
    "cars": [
      "BMW",
      "Audi"
    ]
  }
}
```
it strore data in key value pairs and arrays
 - Data is in key/value pairs
 - Data is separated by commas
 - Curly braces hold objects
 - Square brackets hold array

The most common use of of json data and file is to read data from a server for a website or web application 
