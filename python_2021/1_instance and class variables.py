class Employee():
    no_of_employees=2
    pass
harry=Employee()
rohan=Employee()
harry.name="Harry"
harry.salary=466
harry.role="Instructor"
rohan.name="Rohan"
rohan.salary=45466
rohan.role="Student"
print(rohan.no_of_employees)
#you can change the variable of class by the help of main class only
#you can;t chage by the help of object for eg=rohan.no_of_employees=3 will not affect
Employee.no_of_employees=3
print(rohan.no_of_employees)