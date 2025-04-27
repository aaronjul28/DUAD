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

    def calculate_perimeter_square(self,side1):
        side1=side1
        square_perimeter=side1*4
        return f'The perimeter of the {self.shape} is {square_perimeter}'

    def calculate_perimeter_rectangle(self,weight,height):
            weight=weight
            height=height
            rectangle_perimeter=(weight*2)+(height*2)
            return f'The perimeter of the {self.shape} is {rectangle_perimeter}'

    def calculate_perimeter_circle(self,diameter):
        diameter=diameter
        circle_perimeter=diameter*math.pi
        return f'The perimeter of the {self.shape} is {circle_perimeter}'


    def calculate_area_rectangle_square(self,lenght,width):
        lenght=lenght
        width=width
        area=lenght*width
        return f'The area of the {self.shape} is {area}'
    
    def calculate_area_circle(self,radius):
        radius=radius
        area=(radius*radius)*math.pi
        return f'The area of the {self.shape} is {area}'
        
#INHERIT SHAPE
@abstractmethod
class Circle(Shape):
    def area(self):
        circle_area=self.calculate_area_circle()
        return circle_area

    def perimeter(self):
        circle_perimeter=self.calculate_perimeter_circle()
        return circle_perimeter
@abstractmethod
class Square(Shape):
    def area(self):
        square_area=self.calculate_area_rectangle_square()
        return square_area

    def perimeter(self):
        square_perimeter=self.calculate_perimeter_square()
        return square_perimeter

@abstractmethod
class Rectangle(Shape):
    def area(self):
        rectangle_area=self.calculate_area_rectangle_square()
        return rectangle_area

    def perimeter(self):
        rectangle_perimeter=self.calculate_perimeter_rectangle()
        return rectangle_perimeter



#-------TESTING-------
#RECTANGLE 
rectangle=Rectangle('rectangle')
print(rectangle.calculate_perimeter_rectangle(5,5))
print(rectangle.calculate_area_rectangle_square(5,5))


#SQUARE 
square=Square('square')
print(square.calculate_perimeter_square(5))
print(square.calculate_area_rectangle_square(5,5))

#CIRCLE
circle=Circle('circle')
print(circle.calculate_perimeter_circle(5))
print(circle.calculate_area_circle(5))

