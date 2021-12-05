from application import *

""" Не понял как сделать так, чтобы при таком импорте были узнаваемы модули и функции из них
Для этого нужно добавлять конструкции в init.py? 
Вот такое решение я нашел на StackOverFlow:

__all__ = []

import pkgutil
import inspect

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)

    for name, value in inspect.getmembers(module):
        if name.startswith('__'):
            continue

        globals()[name] = value
        __all__.append(name)
        
        """


