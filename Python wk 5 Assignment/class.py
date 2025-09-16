# Class : Superhero 
class Superhero:  # Defines a new class called Superhero
    # Constructor to initialize attributes
    def __init__(self, name, superpower, level):   
        self.name = name
        self.superpower = superpower
        self.level = level

    def show_info(self):  
        # show_info() prints all the superhero's details
        print(f"Hero: {self.name}")
        print(f"Superpower: {self.superpower}")
        print(f"Level: {self.level}")

    def use_power(self):
        print(f"{self.name} uses {self.superpower}!")


# Villain class inherits from Superhero
class Villain(Superhero):  
    def __init__(self, name, superpower, level, evil_plan):
        super().__init__(name, superpower, level)  
        self.evil_plan = evil_plan  

    def show_info(self):  # Overrides to display villain info
        super().show_info()
        print(f"Evil Plan: {self.evil_plan}")


# Create objects
hero1 = Superhero("StarLord", "Plasma Blast", 9)  
villain1 = Villain("BlackMask", "SuperSerum Punch", 8, "Enemies puke their guts out") 

# Call methods
hero1.show_info()
hero1.use_power()
villain1.show_info()
villain1.use_power()


# ----------------------------
# Assignment 2: Polymorphism with Vehicles
# ----------------------------

class Vehicle:  
    def move(self):
        pass

class Car(Vehicle):  
    def move(self):  
        print("Driving on the road ")

class Plane(Vehicle): 
    def move(self):   
        print("Flying in the sky ")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water ")


# Create a list of different vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Loop through and call move()
for v in vehicles:  
    v.move()
