import math

radius = float(input('Entre the radius of the circle: '))
area = float(input('Enter the area of the circle: '))

circumference = 2 * math.pi * radius
area = math.pi * pow(radius,2)

print(f'The circumferece of the circle is :{round(circumference , 2)}cm')

print (f'The area of the circle is :{round( area , 2)} cm^2')
