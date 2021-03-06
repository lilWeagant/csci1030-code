# File for our Pet class
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