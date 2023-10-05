# https://www.youtube.com/watch?v=vRVVyl9uaZc&list=TLPQMDUxMDIwMjMSC9G60IGTYQ&index=4
from dataclasses import dataclass, field


@dataclass (order=True, frozen=True)
#doesnt need __init__ the decorator already does it for us
class Person:
    sort_index: int = field(init=False, repr=False)

    name:str
    job:str
    age:int
    strength: int = 100

    def __post_init__(self):
        #self.sort_index = self.strength
        # setattr outdoes frozen=True
        object.__setattr__(self, 'sort_index', self.strength)

    #change default representation of print(person1)
    def __str__(self):
        return f'{self.name}, {self.age}, ({self.age})'
    
    '''
    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age
    '''
person1 = Person("A", "a", 1, 99)
person2 = Person("B", "b", 2)
person3 = Person("B", "b", 2)

print(id(person2))
#1227339341536
print(id(person3))
#1227339338320
print(person1)
#Person(name='A', job='a', age=1)

print(person3 == person2)
#True




print(person3 > person1)

















'''
#example
class Person:
    name:str
    job:str
    age:int

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age

person1 = Person("A", "a", 1)
person2 = Person("B", "b", 2)
person3 = Person("B", "b", 2)

print(id(person2))
#1738765967120

print(id(person3))
#1738765966976

print(person1)
#<__main__.Person object at 0x00000194D6871FD0>

print(person3 == person2)
#False

'''