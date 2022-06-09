class Pet:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_mass(self, mass):
        self.mass = mass
    def get_mass(self):
        return self.mass
    def __lt__(self, another_pet):
        return self.get_mass() < another_pet.get_mass()
        # if self.get_mass() < another_pet.get_mass():
        #     return True
        # else:
        #     return False
        # 7 < 8 -> True
        # 8 < 7 -> False

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

# Test code for Cat class
kitty = Cat("Kitty", 14.3)
kitty.set_mass(14.0)
print(kitty)
sasha = Cat("Sasha", 8.0)
print(sasha)

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

# Test code for Dog class
indy = Dog("Indy", 105.2)
print(indy)
turk = Dog("Turk", 130.0)
print(turk)

if kitty < sasha:
    print('Kitty is the smaller cat')
else:
    print('Sasha is the smaller cat')