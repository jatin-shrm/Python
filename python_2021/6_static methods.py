class Employee():
    no_of_employees=2
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    @classmethod
    def change_employee(cls,new_employee):
        cls.no_of_employees=new_employee

    @classmethod
    def class_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
         print("This is good " + string)

harry=Employee("Harry",466,"Instructor")
rohan=Employee("Rohan",43972,"Student")
vijay=Employee.class_str("Vijay-744-Worker")
Employee.printgood("Harry")