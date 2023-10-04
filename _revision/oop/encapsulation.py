#https://www.youtube.com/watch?v=dzmYoSzL8ok
#encapsulation & data hiding
# private attribute:     __

class Human:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

   
    
        '''this will not work'''
        #   h1 = Human(...)  
        #   h1.__name = ""
        ''' we can create properties to allow read&write'''

    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, value):
        if value == "Blob":
            self.__name = "Default Name"
        else:
            self.__name = value

    @staticmethod
    def mymethod():
        print("Hello world")

h1 = Human("Bob", 28, "M")

h1.Name = "Blob"
print(h1.Name)

h1.mymethod()
Human.mymethod()

    

