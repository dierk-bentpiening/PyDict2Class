'''
DictObject Mappper
(C) 2023 Dierk-Bent Piening
E-Mail: dierk-bent.piening@mailbox.org
Licensed under the GNU Lesser General Public License

@package pydict2class
'''
from json import dumps
import logging
import builtins
from datetime import datetime

class PyDict2Class:
    def __init__(self, debug: bool = False)-> None:
        self._logger: object = logging.getLogger("Dict2Class")
        self._type_dict: dict[object, object] = {}
        
        if debug:
            self._logger.setLevel(logging.DEBUG)
    @property
    def types(self) -> dict:
         return self._type_dict

    @types.setter
    def types(self, value) ->  None:
        if isinstance(value, list):
            for typedef in value:
                self._type_dict[typedef.__class__.__name__] = value
        else:
            self._type_dict[value.__class__.__name__] = value


    class BaseClass(object):
        _dynamic_class: bool = True
        _created: datetime = datetime.now()
        _init: bool = False
        _init_datetime: datetime = None

        def __init__(self, **kwargs) -> None:
            pass

    def generate(self, condict, classname: str,  BaseClass=BaseClass, json: bool = False, prioritizetypedict: bool = False) -> object:
        def __init__(self, **kwargs):
            self.__class__ = self.__class__
            for key, value in kwargs.items():
                setattr(self, key, value)
            self._init = True
            self._init_datetime = datetime.now()
            BaseClass.__init__(self, **kwargs)
        classattributes: dict = {"__init__": __init__}
        if (isinstance(condict, str)) and (json is True):
            condict = dumps(condict)
        if isinstance(condict, dict):
            for key, value in condict.items():
                if prioritizetypedict:
                    if self._type_dict.get(value.__class__.__name__):
                        classattributes[key] = self._type_dict.get(value.__class__.__name__)
                    else:
                        self._logger.error(f"Type of {value} is not in type dict!")
                        try:
                            builtintype = getattr(builtins, value.__class__.__name__)
                        except AttributeError:
                            self._logger.debug(f"Type of {value} is not part of builtinns")
                            raise TypeError
                        else:
                            classattributes[key] = builtintype
                else:
                    try:
                        builtintype = getattr(builtins, value.__class__.__name__)
                    except AttributeError:
                        self._logger.debug(f"Type of {value} is not part of builtins!")
                        if self._type_dict.get(value.__class__.__name__):
                            classattributes[key] = self._type_dict.get(value.__class__.__name__)
                        else:
                            raise AttributeError
                            self._logger.error(f"Type of {value} is not in type dict!")
                    else:
                        classattributes[key] = builtintype
            return type(classname, (BaseClass,), classattributes)
        else:
            raise TypeError

    def generate_and_fill(self, condict, classname: str,  BaseClass=BaseClass, type_dict=None, json=False, prioritizetypedict: bool = False ) -> object:
        genclass = self.generate(condict, classname, BaseClass, type_dict=None, json=json, prioritizetypedict=prioritizetypedict)
        return genclass(**condict)



