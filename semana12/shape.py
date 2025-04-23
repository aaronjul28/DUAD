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

    def calculate_perimeter(self):
        if self.shape=='square':
            side1=int(input('Enter the size of either of the sides: '))
            square_perimeter=side1*4
            return f'The perimeter of the {self.shape} is {square_perimeter}'
        
        if self.shape=='rectangle':
            weight=int(input('Enter the size of the weight: '))
            height=int(input('Enter the size of the height: '))
            rectangle_perimeter=(weight*2)+(height*2)
            return f'The perimeter of the {self.shape} is {rectangle_perimeter}'

        if self.shape=='circle':
            diametro=int(input('Enter the diameter of the circle: '))
            circle_perimeter=diametro*math.pi
            return f'The perimeter of the {self.shape} is {circle_perimeter}'


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

    def perimeter(self):
        circle_perimeter=self.calculate_perimeter()
        return circle_perimeter

class Square(Shape):
    def area(self):
        square_area=self.calculate_area()
        return square_area

    def perimeter(self):
        square_perimeter=self.calculate_perimeter()
        return square_perimeter

class Rectangle(Shape):
    def area(self):
        rectangle_area=self.calculate_area()
        return rectangle_area

    def perimeter(self):
        rectangle_perimeter=self.calculate_perimeter()
        return rectangle_perimeter



#-------TESTING-------
#RECTANGLE AREA
rectangle=Rectangle('rectangle')
print(rectangle.area())
print(rectangle.perimeter())

#RECTANGLE PERIMETER



#SQUARE AREA
square=Square('square')
print(square.area())
print(square.perimeter())

#CIRCLE AREA
circle=Circle('circle')
print(circle.area())
print(circle.perimeter())
