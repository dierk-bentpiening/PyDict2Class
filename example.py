from pydict2class import PyDict2Class

if __name__ == "__main__":
    dict2class = PyDict2Class()
    mydict = {"string": "this is a string", "integer": 12341, "boolean": True, "listofint": [1,2,3,4,5,6,7,8,9]}
    myclass = dict2class.generate(mydict, "testclass")
    print(type(myclass))
    myobj = myclass(string="teststring")
    print(myobj)
    print(myobj.string)
    myobj2 = dict2class.generate_and_fill(mydict, "testclass")
    print(myobj2)
    print(myobj2.string)
    print(myobj2.integer)
    print(myobj2.boolean)
    print(myobj2.listofint)
    print(myobj2._created)
    print(myobj2._init_datetime)
