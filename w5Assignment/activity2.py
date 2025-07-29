#-------------------------------------------------------------    
#Activity 2: Polymorphism Challenge! 🎭

#5.Create a program that includes animals or vehicles with the same action (like move()).
#6.However, make each class define move() differently
#7.(for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
    
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is moving..."

class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving on the road."
    
class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying in the sky."

class Bicycle(Vehicle):
    def move(self):
        return f"{self.name} is pedaling down the street."

#Testing the polymorphism
vehicles = [Car("Mercedes S-class"), Plane("Boeing 747"), Bicycle("Mountain Bike")]

for v in vehicles:
    print(v.move())
