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
        params=string.split("-")
        return cls(params[0], params[1], params[2])
    # or you can do this in one line
        #return cls(*string.split("-"))

harry=Employee("Harry",466,"Instructor")
rohan=Employee("Rohan",43972,"Student")
vijay=Employee.class_str("Vijay-744-Worker")
harry.change_employee(3)
print(vijay.salary)