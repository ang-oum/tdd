#https://www.youtube.com/watch?v=Qb4rMvFRLJw&list=TLPQMDMxMDIwMjPGzxZERpF2sg&index=9
#
#class that can only have one single instance
#
#1person object

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        '''implement in child class'''

#many ways: decorators, own metaclass etc
#
#one way >>
class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        #only instance
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name} Age: {PersonSingleton.__instance.age}")

p = PersonSingleton("Bob", 24)
print(p)
p.print_data()


#not possible to create a second instance
p2 = PersonSingleton.get_instance()
print(p2)
p2.print_data()
    