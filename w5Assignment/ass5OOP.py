#Assignment 1: Design Your Own Class! 🏗️
#1.Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
#2.Add attributes and methods to bring the class to life!
#3.Use constructors to initialize each object with unique values.
#4.Add an inheritance layer to explore polymorphism or encapsulation.

#Base class
class Superhero:
    def __init__(self,name, power_level):
        self.name = name   #Attr
        self._power_level = power_level #Encapsulation
        
    def speak(self):
        return f"I am {self.name}, a protector of the city" 
    
    def get_power_level(self):
        return self._power_level
    
    def attack(self):
        return f"{self.name} attack with a standard punch!"   
    
   
class Batman(Superhero):
    def __init__(self, name="Batman", power_level=85):
        super().__init__(name, power_level)
        self.__gadgets = ['Batarang', 'Grapple Gun', 'Smoke Bomb'] #private attribute
        self.vehicle = "Batmobile"
    
    def attack(self):
        return f"{self.name} uses {self.__gadgets[0]} to disable the enemy!" #Polymorphism   
    
    def stealth(self):
        return f"{self.name} disappears into the shadows."
    
    def reveal_gadgets(self):
        return f"Gadgets: {','.join(self.__gadgets)}" 
    
class Superman(Superhero):
    def __init__(self, name="Superman", power_level=100):
        super().__init__(name, power_level)
        self.flying_speed = "Superfast"
        
    def attack(self):
        return f"{self.name} uses laser eyes!" #same fn different behaviour
    
    def fly(self):
        return f"{self.name} is flying at {self.flying_speed} speed!"
    
#Polymorphism
heroes = [Batman(),Superman()]

for hero in heroes:
    print(hero.attack())       


    