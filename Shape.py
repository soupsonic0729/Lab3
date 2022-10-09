from abc import ABCMeta, abstractmethod
import math

class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_dimensions(self):
        pass

class Square(Shape):
    def __init__(self, color, length_side):
        super().__init__(color)
        self.__length_side = length_side

    def get_area(self):
        return self.__length_side * self.__length_side

    def get_perimeter(self):
        return self.__length_side * 4

    def get_dimensions(self):
        return self.__length_side

    def __str__(self):
        return "The Color: " + str(self.get_color()) + " The Dimension: " + str(self.get_dimensions()) + \
               " The Area: " + str(self.get_area()) + " The Perimeter: " + str(self.get_perimeter())

    def __repr__(self):
        return "Square(" + str(self.__length_side) + ")"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius

    def get_area(self):
        return self.__radius * self.__radius * math.pi

    def get_perimeter(self):
        return self.__radius * 2 * math.pi

    def get_dimensions(self):
        return self.__radius

    def __str__(self):
        return "The Color: " + str(self.get_color()) + " The Dimension: " + str(self.get_dimensions()) + \
               " The Area: " + str(self.get_area()) + " The Perimeter: " + str(self.get_perimeter())

    def __repr__(self):
        return "Circle(" + self.__radius + ")"

class Triangle(Shape):
    def __init__(self, color, length_side1, length_side2, length_side3):
        super().__init__(color)
        self.__length_side1 = length_side1
        self.__length_side2 = length_side2
        self.__length_side3 = length_side3
        self.__length_side_array = [length_side1, length_side2, length_side3]


    def get_area(self):
        s = (self.__length_side_array[0] + self.__length_side_array[1] + self.__length_side_array[2]) / 2

        return math.sqrt(s * (s - self.__length_side_array[0]) * (s - self.__length_side_array[1]) * (s - self.__length_side_array[2]))

    def get_perimeter(self):
        return self.__length_side_array[0] + self.__length_side_array[1] + self.__length_side_array[2]

    def get_dimensions(self):
        return self.__length_side_array

    def __str__(self):
        return "The Color: " + str(self.get_color()) + " The Dimension: " + str(self.get_dimensions()) + \
               " The Area: " + str(self.get_area()) + " The Perimeter: " + str(self.get_perimeter())

    def __repr__(self):
        return "Triangle(" + str(self.__length_side_array[0]) + ", " + str(self.__length_side_array[1]) + ", " + str(self.__length_side_array[2]) + ")"

# square1 = Square("Red", 47)
# circle1 = Circle("Blue", 23.5)
#
# print("the area of the square is: " + str(square1.get_area()))
# print("the area of the circle is: " + str(circle1.get_area()))
# print("the area of the wasted material is: " + str(math.floor((square1.get_area() - circle1.get_area()) * 10 ** 3)/(10 ** 3)))
#
# print(square1.__str__())

triangle1 = Triangle("Red", 3, 4, 5)
triangle2 = Triangle("Blue", 19, 19, 19)
triangle3 = Triangle("Yellow", 4, 4, 5)

# print(triangle1.__str__())
# print(triangle2.__str__())
# print(triangle3.__str__())

triangle_list = [triangle1, triangle2, triangle3]

for i in range(3):

     if triangle_list[i].get_dimensions()[0] == triangle_list[i].get_dimensions()[1] == \
             triangle_list[i].get_dimensions()[2]:
         print(triangle_list[i].__repr__() + " is an Equilateral Triangle")

     elif triangle_list[i].get_dimensions()[0] == triangle_list[i].get_dimensions()[1] or \
             triangle_list[i].get_dimensions()[1] == triangle_list[i].get_dimensions()[2] or \
             triangle_list[i].get_dimensions()[2] == triangle_list[0]:
         print(triangle_list[i].__repr__() + " is an Isosceles Triangle")

     else:
         print(triangle_list[i].__repr__() + " is Scalene Triangle")

