#https://www.youtube.com/watch?v=iSG87hpAFhQ&list=TLPQMDMxMDIwMjPGzxZERpF2sg&index=10
#
#multiple classes that inherit from same interface or parent class
# one of those can exist of many subcomponents
#
#parent>multiple>sub-multiple
#
#increase flexibility
#
#easier to use

from abc import ABCMeta, abstractmethod, abstractstaticmethod

class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        '''implement in child class'''

    @abstractstaticmethod
    def print_department():
        '''implement in chimd class'''




class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting department: {self.employees}")

class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development department: {self.employees}")







class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees
    
    def print_department(self):
        print("Parent Department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of employees: {self.employees} ")




dept1 = Accounting(200)
dept2 = Development(400)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()





