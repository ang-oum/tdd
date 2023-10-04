import mypy

def myfunction(myparameter: int) -> int:
    print(myparameter)

myfunction("Hello world")
    

#CLI: mypy typehinting.py
'''
error: Argument 1 to "myfunction" has incompatible type "str"; expected "int"
'''

def function(otherparameter: str):
    print(otherparameter)

function(myfunction(20))
'''
error: Argument 1 to "function" has incompatible type "int"; expected "str"
'''

def dosmth(param: list[int]):
    return