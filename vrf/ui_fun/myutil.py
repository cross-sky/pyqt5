'''
Author: your name
Date: 2022-05-16 23:21:12
LastEditTime: 2022-05-16 23:42:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \\pyqt5\\vrf\\ui_fun\\util.py
'''
class _const:
    class ConstError(TypeError): pass
    def __setattr__(self, name: str, value) -> None:
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const ({})".format(name))
        self.__dict__[name] = value

class Const:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Const, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
    
    class ConstError(TypeError):
        def __init__(self, name):
            self.msg = "Can't rebind const instance attribute (%s)"%name
    
        def __str__(self):
            return 'error msg: {}'.format(self.msg)

        def __repr__(self):
            return self.__str__()

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError(name)
        self.__dict__[name] = value

    def __delattr__(self, name):
        if self.__dict__.has_key(name):
            raise self.ConstError(name)
        raise self.ConstError(name)
    
