# Cree una clase abstracta de Shape que:
# 1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
# 2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
# 3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod
import math


class Shape():
    @abstractmethod
    def calculate_perimeter():
        pass

    @abstractmethod
    def calculate_area():
        pass

class Circle(Shape):
    def calculate_perimeter(self,diameter):
        perimeter=diameter*math.pi
        return f'The perimeter of the circle is {perimeter}'

    def calculate_area(self,radius):
        area=(radius*radius)*math.pi
        return f'The area of the circle is {area}'

class Square(Shape):
    def calculate_perimeter(self,side):
        perimeter=side*4
        return f'The perimeter of the square is {perimeter}'

    def calculate_area(self,lenght,width):
        area=lenght*width
        return f'The area of the square is {area}'

class Rectangle(Shape):
    def calculate_perimeter(self,lenght,width):
        perimeter=(lenght*2)+(width*2)
        return f'The perimeter of the rectangle is {perimeter}'

    def calculate_area(self,lenght,width):
        area=lenght*width
        return f'The area of the rectangle is {area}'


circle_perimeter=Circle()
print(circle_perimeter.calculate_perimeter(5))
print(circle_perimeter.calculate_area(5))

square_perimeter=Square()
print(square_perimeter.calculate_perimeter(5))
print(square_perimeter.calculate_area(5,5))


square_perimeter=Rectangle()
print(square_perimeter.calculate_perimeter(5,5))
print(square_perimeter.calculate_area(5,5))


