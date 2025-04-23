# Cree una clase abstracta de Shape que:
# 1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
# 2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
# 3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod
import math

#ABSTRACT PARENT
class Shape(ABC):

    def __init__(self,shape):
        self.shape=shape

    def calculate_perimeter():
        pass
            

    def calculate_area(self):
        #TEST IF THE SHAPE IS BEING LEARNED CORRECTLY
        #print(self.shape)
        if self.shape=='rectangle' or self.shape=='square':
            lenght=int(input('Enter the lenght: '))
            width=int(input('Enter the width: '))
            area=lenght*width
            return f'The area of the {self.shape} is {area}'
#return f'The area of {self.shape} is {area}'        
        if self.shape=='circle':
            radius=int(input('Enter the radius of the circle: '))
            area=(radius*radius)*math.pi
            return f'The area of the {self.shape} is {area}'
        
#INHERIT SHAPE
class Circle(Shape):
    def area(self):
        circle_area=self.calculate_area()
        return circle_area

class Square(Shape):
    def area(self):
        square_area=self.calculate_area()
        return square_area

class Rectangle(Shape):
    def area(self):
        rectangle_area=self.calculate_area()
        return rectangle_area

#RECTANGLE AREA
rectangle_area=Rectangle('rectangle')
print(rectangle_area.area())

#SQUARE AREA
square_area=Square('square')
print(square_area.area())

#CIRCLE AREA
circle_area=Circle('circle')
print(circle_area.area())
