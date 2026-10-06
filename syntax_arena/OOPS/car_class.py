class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        
    def display_info(self):
        print(f"This is a {self.color} {self.brand}")
        
        
car1 = Car("BWM","Red")
car2 = Car("Mercedes","Black")

car1.display_info()
# Car.display_info(car1)
car2.display_info()
# Car.display_info(car2)


class FlyingCar(Car):
    def __init__(self,wings,color):
        self.wings = wings
        self.color = color
        
f1_car = FlyingCar("4 Wings","Blue")

print(f1_car.wings)
print(f1_car.color)


        




