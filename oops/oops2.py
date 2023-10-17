#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
model=Bus("Toyota",200,40)
print(f"Vehicle name {model.name}, max speed is {model.max_speed} and mileage is {model.mileage}")