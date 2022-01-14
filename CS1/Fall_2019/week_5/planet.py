# planet.py
# Class for planets.

class Planet:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def mass_eq(self, other):
        return self.mass == other.mass

    def name_eq(self, other):
        return self.name.lower() == other.name.lower()

    def mass_ne(self, other):
        return self.mass == other.mass

    def name_ne(self, other):
        return self.name.lower() != other.name.lower()

    def mass_lt(self, other):
        return self.mass < other.mass

    def name_lt(self, other):
        return self.name.lower() < other.name.lower()

    def mass_gt(self, other):
        return self.mass > other.mass

    def name_gt(self, other):
        return self.name.lower() > other.name.lower()

    def mass_le(self, other):
        return self.mass <= other.mass

    def name_le(self, other):
        return self.name.lower() <= other.name.lower()

    def mass_ge(self, other):
        return self.mass >= other.mass

    def name_ge(self, other):
        return self.name.lower() >= other.name.lower()

    def __str__(self):
        return self.name + ": " + str(self.mass)