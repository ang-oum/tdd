# Factory design pattern = one of many OO design patterns
# goel increase modularoty, increase seperation of concerns
# individual classes, modules etc
# for large projects
# increasing complexity, decreasing readability



from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        ''' Interface method'''
        #defenition of the signature
        '''
        p1 = IPerson()
        p1.person_method()
        #Not possible, its an abstract class, eg not able to create instances of it
        
        #TypeError: Can't instantiate abstract class IPerson 
        
        '''

class Student(IPerson):

    def __init__(self):
        self.name = "Basic Student Name"

    #override:
    def person_method(self):
        print("I am a student")

class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Name"
    
    def person_method(self):
        print("I am a teacher")




'''
s1 = Student()
s1.person_method()

t1 = Teacher()
t1.person_method()
'''




class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1

if __name__ == "__factorydesign__":
    choice = input("What type of person do u want to create? \n")
    person = PersonFactory.build_person(choice)
    person.person_method()


# Dynamically decide if we want to build a or b during runtime






