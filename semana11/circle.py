class Circle:
    radius=input('Please enter the radius of the circle: ')
    radius=int(radius)
    def get_area(radius):
        area= (radius*radius)*3.14
        print(f'The area of the circle is {area}')
    get_area(radius)
    
Circle()

