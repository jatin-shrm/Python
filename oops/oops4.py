#use of super
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show_info(self):
        return f"Employee name is {self.name} and age is {self.age}"
class Programmer(Employee):
    def __init__(self, name, age,language):
        super().__init__(name, age)
        self.language=language

    def show_info(self):
        return f"Employee name is {self.name} and age is {self.age} and language is {self.language}"

e1=Employee("Jatin",20)
print(e1.show_info())
p1=Programmer("Rahul",22,"Python")
print(p1.show_info())