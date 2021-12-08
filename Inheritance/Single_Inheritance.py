class Employee():
    no_of_employees=2
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"The name is {self.name}. The salary is {self.salary}. The role is {self.role}"
    @classmethod
    def change_employee(cls,new_employee):
        cls.no_of_employees=new_employee

    @classmethod
    def class_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
         print("This is good " + string)

class Programmer(Employee):
    def __init__(self,aname,asalary,arole,alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages=alanguages

    def printprog(self):
        return  f"The Programmers is {self.name}. The salary is {self.salary}. The role is {self.role}. The languages are {self.languages}"

harry=Employee("Harry",466,"Instructor")
rohan=Employee("Rohan",43972,"Student")

aman=Programmer("Aman",432,"Programmer",["Python","PhP"])
vijay=Programmer("Vijay",59,"Programmer",["Python","C++"])
print(vijay.printprog())
