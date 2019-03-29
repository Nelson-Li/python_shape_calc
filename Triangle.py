

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def set_base(self, base):
        self.base = base

    def set_height(self, height):
        self.height = height

    def calc_area(self, base, height):
        area = 0.5 * base * height
        return area
