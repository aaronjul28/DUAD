# class Circle:
#     radius=input('Please enter the radius of the circle: ')
#     radius=int(radius)
#     def get_area(radius):
#         area= (radius*radius)*3.14
#         print(f'The area of the circle is {area}')
#     get_area(radius)
    
# Circle()

import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
        self.radius=int(radius)

    def get_area(self):
        radius=self.radius
        area= (radius*radius)*math.pi
        return area
    
circle=Circle(input('Enter the radius:'))
print(circle.get_area())

