
#__________________________________________________________________
# practical Example #2 - Timing
#__________________________________________________________________


import time

def timed(function):
    def wrapper(*args,**kwargs):
        before = time.time()
        value = function(*args,**kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute!")
        return value
    return wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result



print(myfunction(100))















#
print('\n')
#__
#__________________________________________________________________
# practical Example #1 - Logging
#__________________________________________________________________

def logged(function):

    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}")
        return value
    return wrapper

@logged
def add(x, y):
    return x + y

print(add(10,20))
























#
print('\n')
#__________________________________________________________________
# basic idea behind decorators
#__________________________________________________________________

def mydecorator(function):

    def wrapper(*args, **kwargs):
        
        print("I'm decorating your function")
        """"""# function(*args, **kwargs)
        return function(*args, **kwargs)
        
    
    return wrapper
# we're not just executing this, we're actually returning the wrapper function
# we're returning another function that calls the initial function 
# but with decorated code

def hello_world():
    print("Hello world")


#calling the function, passing a fuction, then calling the result
mydecorator(hello_world)()
# this is not how its done in python
# more elegant way:
'''
@mydecorator
def hi_world():
    print("Hi world")

hi_world()
'''


#__________________________
# limitations: parametres should be same for wrapper&decorator
@mydecorator
def hello(person):
    """"""#print(f"Hello {person}!")
    return f"Hello {person}!"

""""""#hello("Mike")
print(hello("Mike"))
'''
TypeError: wrapper() takes 0 positional arguments but 1 was given
'''
#--> wrapper(*args, **kwargs)