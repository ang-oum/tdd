#Odoo provides support for testing modules using Python’s unittest library.
"""
To write tests:

simply define a 'tests' sub-package in your module, 
it will be automatically inspected for test modules. 
Test modules should have a name starting with test_ and should be imported from tests/__init__.py, e.g.
"""
#           your_module
#           ├── ...
#           ├── tests
#           |   ├── __init__.py
#           |   ├── test_bar.py
#           |   └── test_foo.py
'''
__init__.py
contains:
from . import test_foo, test_bar
'''