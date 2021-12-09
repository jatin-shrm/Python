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

class Player:
    no_of_game=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f"The name is {self.name}. The game is {self.game}."

class CoolProgrammer(Employee,Player):
    language = "Python"
    def printlanguage(self):
        print(self.language)

harry=Employee("Harry",466,"Instructor")
rohan=Employee("Rohan",43972,"Student")

shubham=Player("SHubham",["Cricket"])
vijay=CoolProgrammer("Vijay",677687,"Cool Programmer")
print(vijay.language)
print(vijay.printdetails())