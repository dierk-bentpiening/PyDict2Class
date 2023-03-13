# PyDict2Class
 Dynamic create classes from dict or json like you would develop them yourself.

## Introduction
This tool makes it possible to generate a Python class with attributes from a dict or a JSON, or to create an object with the corresponding assigned values.
The data type of the value of the dict or JSON is recognized and automatically initialized with the appropriate builtins data types.
Non Python standard types or methods can also be included by adding them to the type attribute, this can also override the internal data types.

i use this tool to dynamically create mongoengine data classes with the appropriate attributes.
Actual i am implement the Functionality to create SQLAlchemy Data Model classes.
## Usage
install the library from source or over pip.
import package and inherit Class object.

```python:
from pydict2class import Dict2Class
dict2class = Dict2Class()
```

Define the Dictionary you want to generate a class from.
```python:
mydict = {"integer": 1, "string": "my string", "boolean": True, "list": [1, 2, 3]}
```
Now you have to decide whether you want to generate only the class or if you want to generate the class and instantiate it with the values given in your dict or json.

**Only generate the class:**
```python:
myclass = dict2class.generate(mydict, "myclassname")
```
The magic is done and you have a dynamic class with the dictionary keys as attribute names and the value data type as datatype.


**Generate class and initialize object:**
