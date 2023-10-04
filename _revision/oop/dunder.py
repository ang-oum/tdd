class Person:
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #deconstructor
    def __del__(self):
        print("Object is being deconstructed")

p = Person("Mike", 25)

#________________________________________________________






#____________________________________________________________
# operator overloading
#____________________________________________________________
'''
__add__()
__sub__()
'''







class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    ''''''''''''
    def __add__(self, other):
        #other also has to be a vector
        #which we are not checking since python is dynamically written (so we can also pass anything else)
        return Vector(self.x + other.x, self.y + other.y)
    ''''''''''''
    def __sub__(self, other):
        #other also has to be a vector
        #which we are not checking since python is dynamically written (so we can also pass anything else)
        return Vector(self.x - other.x, self.y - other.y)
    ''''''''''''
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"
    ''''''''''''
    def __len__(self):
        print("opens ability to return length of object if Vector object ")
        return 10
    ''''''''''''
    def __call__(self):
        print("I was called")
       




v1 = Vector(10, 20)
v2 = Vector(50,60)
v3 = v1 + v2
'''
TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
'''
#--> __add__
print(v3.x)
print(v3.y)
###################################################
print(v3)
'''
<__main__.Vector object at 0x000001A19EB95CD0>
'''
#--> __str__
#--> __repr__
'''

'''
print(len(v3))
'''

'''
v3()


