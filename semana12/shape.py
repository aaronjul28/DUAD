# Cree una clase abstracta de Shape que:
# 1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
# 2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
# 3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self,radius,diameter):
        self.radius=radius
        self.diameter=diameter

    def calculate_perimeter(self):
        perimeter=self.diameter*math.pi
        return f'The perimeter of the circle is {perimeter}'

    def calculate_area(self):
        area=(self.radius*self.radius)*math.pi
        return f'The area of the circle is {area}'

class Square(Shape):

    def __init__(self,side):
        self.side=side

    def calculate_perimeter(self):
        perimeter=self.side*4
        return f'The perimeter of the square is {perimeter}'

    def calculate_area(self):
        area=self.side*self.side
        return f'The area of the square is {area}'

class Rectangle(Shape):

    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width

    def calculate_perimeter(self):
        perimeter=(self.lenght*2)+(self.width*2)
        return f'The perimeter of the rectangle is {perimeter}'

    def calculate_area(self):
        area=self.lenght*self.width
        return f'The area of the rectangle is {area}'


circle_perimeter=Circle(5,5)
print(circle_perimeter.calculate_perimeter())
print(circle_perimeter.calculate_area())

square_perimeter=Square(5)
print(square_perimeter.calculate_perimeter())
print(square_perimeter.calculate_area())


square_perimeter=Rectangle(5,5)
print(square_perimeter.calculate_perimeter())
print(square_perimeter.calculate_area())


