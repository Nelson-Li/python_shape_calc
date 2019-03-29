import FileIO
import Circle
import Rectangle
import Triangle


def main():
    print("Choose from the following calculation options:\n")
    user_input = input("1. Circle:\n"
                       "2. Rectangle:\n"
                       "3. Triangle:\n")

    file_input = input("Enter file for calculation:\n")
    fields = FileIO.read(file_input)
    f_length = len(fields)
    if int(user_input) == 1:
        circle = Circle.Circle("Diameter")
        for i in range(f_length):
            diameter = int(fields[i].pop(0))
            area = Circle.Circle.calc_area(circle, diameter)
            print(area)
    elif int(user_input) == 2:
        rectangle = Rectangle.Rectangle("Length", "Width")
        for i in range(f_length):
            length = float(fields[i].pop(0))
            width = float(fields[i].pop(0))
            area = Rectangle.Rectangle.calc_area(rectangle, length, width)
            print(area)
    elif int(user_input) == 3:
        triangle = Triangle.Triangle("Base", "Width")
        for i in range(f_length):
            base = float(fields[i].pop(0))
            height = float(fields[i].pop(0))
            area = Triangle.Triangle.calc_area(triangle, base, height)
            print(area)
    else:
        print("Invalid:\n")


if __name__ == '__main__':
    main()
