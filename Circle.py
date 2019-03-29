import math


class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    def set_diameter(self, diameter):
        self.diameter = diameter

    def validate_diameter(self):
        if self.diameter >= 0:
            return self.diameter
        else:
            print("Invalid input for diameter:\n")

    def calc_area(self, diameter):
        area = math.pi * math.pow(diameter / 2, 2)
        return area
