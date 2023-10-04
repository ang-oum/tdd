class Friend:
    #Class variables are variables that arent unique per object but
    #The same for each object
    humans = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Friend.humans += 1

    def __str__(self):
        return "Name:{}, Age:{}, Height:{}".format(self.name, self.age, self.height)
        '''
        TypeError: __str__ returned non-string (type NoneType)
        '''
        #--> use return instead of print()
    
    def __del__(self):
        print("Object deleted")
        Friend.humans -= 1
    
    def helloWorld(self):
        print("Hello world")

    def get_older(self, years):
        self.age += years
    
    
        
friend1 = Friend("Bob", 24, 180)

print(friend1.name)
print(friend1.age)
print(friend1.height)

friend1.name = "Bobina"
print(friend1.name)

friend1.helloWorld()

print(friend1)
'''
<__main__.Friend object at 0x0000027D39264FD0>
'''
#__str__

print(friend1.humans)



del friend1
print(Friend.humans)

