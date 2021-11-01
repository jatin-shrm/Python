class Employee():
    no_of_employees=2
    #constructor is a method to give argument to instance
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
harry=Employee("Harry",466,"Instructor")
print(harry.salary)
