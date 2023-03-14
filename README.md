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
e builtins data types. Non Python standard types or methods can also be inc
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
```
myobj = dict2class.generate_and_init(mydict, "classfdict")
```

**Use JSON instead of Dict:**
```python:
myjsonstr = '{"integer": 1, "string": "my string", "boolean": True, "list": [1, 2, 3]}'
myclass = dict2class.generate(myjsonstr, "myclass", json=True)
```

**Add Custom methods to types and use them:**
```python:
    dict2class = Dict2Class()
    dict2class.types = mycustommethods
    
```
**Add list of custom methods to type and use them:**
```python:
    dict2class = Dict2Class()
    dict2class.types = [custommethod1, custommethod2, custommethod3, custommethod4, custommethod5]
```
## Documentation for PyDict2Class:

This module provides a class called PyDict2Class that allows you to dynamically generate Python classes from dictionaries. The generated classes can be used to create objects based on the key-value pairs in the dictionary.

### PyDict2Class class:

The PyDict2Class class has the following methods:

**init(self, debug: bool = False)** - Constructor method that initializes the PyDict2Class object. It takes an optional parameter 'debug' which, if set to True, enables debug logging.

**types** - Property that returns the type dictionary maintained by PyDict2Class. The type dictionary maps class names to their corresponding types.

**types.setter** - Property setter method that allows you to update the type dictionary maintained by PyDict2Class.

**generate(self, condict, classname: str, BaseClass=BaseClass, json: bool = False, prioritizetypedict: bool = False)** - Method that generates a new class dynamically based on the key-value pairs in the input dictionary 'condict'. The generated class is assigned the name 'classname'. The optional parameter 'BaseClass' allows you to specify a base class that the generated class should inherit from. The optional parameter 'json' allows you to specify whether the input dictionary 'condict' is a JSON string. The optional parameter 'prioritizetypedict' specifies whether to prioritize the type dictionary maintained by PyDict2Class over the built-in types when mapping values to their corresponding types.

**generate_and_fill(self, condict, classname: str, BaseClass=BaseClass, type_dict=None, json=False, prioritizetypedict: bool = False)** - Method that generates a new class dynamically based on the key-value pairs in the input dictionary 'condict', and then instantiates an object of the generated class with the input dictionary as the constructor arguments. The optional parameter 'type_dict' allows you to specify a type dictionary to use for type mapping. The optional parameter 'json' allows you to specify whether the input dictionary 'condict' is a JSON string. The optional parameter 'prioritizetypedict' specifies whether to prioritize the type dictionary maintained by PyDict2Class over the built-in types when mapping values to their corresponding types.

### BaseClass class:

The BaseClass class is a helper class that is used as a base class for the dynamically generated classes. It has the following attributes:

**_dynamic_class** - Boolean attribute that indicates whether the class is dynamically generated or not.

**_created** - Datetime attribute that records the creation time of the object.

**_init** - Boolean attribute that indicates whether the object has been initialized or not.

**_init_datetime** - Datetime attribute that records the initialization time of the object.

**init(self, kwargs)** - Constructor method that initializes the object with the input keyword arguments.

### Example usage:

**Here is an example of how to use PyDict2Class to generate a class dynamically based on a dictionary:**

```python:
from pydict2class import PyDict2Class

# Create a PyDict2Class object
pdc = PyDict2Class()

# Define a dictionary
d = {"name": "Alice", "age": 30}

# Generate a class dynamically based on the dictionary
Person = pdc.generate(d, "Person")

# Create an object of the generated class
alice = Person(name="Alice", age=30)

# Print the object
print(alice)

```

This will output:

```python:
<__main__.Person object at 0x7f7c4c4b6048>
```