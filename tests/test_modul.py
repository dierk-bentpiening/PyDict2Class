import pytest

class TestLib:
    from pydict2class import PyDict2Class
    dict2class = PyDict2Class()
    testdict = {"integer": 1234, "string": "teststring", "boolean": True, "list": [1,2,3,4,5,6,7,8,9,10]}
    myclass = dict2class.generate(testdict,"testclass")
    myobj = myclass(**testdict)
    
    def test_callable(self) -> None:
        assert callable(self.myclass) is True, "Check that generated object is callable"

    def test_modul(self) -> None:
        assert isinstance(self.myobj, self.myclass) is True, "Check that obj is instance of pydict2class generated class"
        
    def test_value(self) -> None:
        assert self.myobj.integer == 1234, "Check that auto setted value matches expected value"
        
    def test_change_value(self) -> None:
        self.myobj.integer = 5
        assert self.myobj.integer == 5, "Check that  setted value matches expected value"
