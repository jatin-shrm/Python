class Employee():
    no_of_employees=2
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    #it is method of changing in attributes of class and it only takes class as a input
    @classmethod
    def change_employee(cls,new_employee):
        cls.no_of_employees=new_employee
harry=Employee("Harry",466,"Instructor")
rohan=Employee("Rohan",43972,"Student")
harry.change_employee(3)
print(rohan.no_of_employees)