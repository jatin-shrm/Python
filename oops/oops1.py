#Create a Class with instance attributes with max_speed and mileage instance attributes
class vehicle:
    def __init__(self,max_speed,mileage) -> None:
        self.max_speed=max_speed
        self.mileage=mileage
model=vehicle(240,40)
print(model.max_speed,model.mileage)