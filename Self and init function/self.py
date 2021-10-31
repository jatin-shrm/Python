class Employee():
    no_of_employees=2
    #self is used for the function on wich you want to perform that task
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}"
harry=Employee()
rohan=Employee()
harry.name="Harry"
harry.salary=466
harry.role="Instructor"
rohan.name="Rohan"
rohan.salary=45466
rohan.role="Student"
print(rohan.printdetails())
