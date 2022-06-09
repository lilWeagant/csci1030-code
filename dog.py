# File for Dog class
from pet import Pet

class Dog(Pet):
    def __init__(self, name, mass):
        Pet.__init__(self, name, mass)
    # def set_name(self, name):
    #     self.name = name
    # def get_name(self):
    #     return self.name
    # def set_mass(self, mass):
    #     self.mass = mass
    # def get_mass(self):
    #     return self.mass
    def __str__(self):
        return "Dog: " + self.name + " weighs " + str(self.mass) + "lbs"