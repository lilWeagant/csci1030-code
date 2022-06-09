# File for our Cat class
from pet import Pet

class Cat(Pet):
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
        return "Cat: " + self.name + " weighs " + str(self.mass) + "lbs"