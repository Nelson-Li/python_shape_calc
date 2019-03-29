
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def validate_parameters(self):
        return self.length >= 0 & self.width >= 0

    def calc_area(self, length, width):
        area = length * width
        return area
