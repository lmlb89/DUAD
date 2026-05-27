

# 1. Cree una clase de `Circle` con:
#    1. Un atributo de `radius` (radio).
#    2. Un método de `get_area` que retorne su área.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  
    
    def get_area(self):
        area = math.pi * self.radius ** 2 
        print(f"The area of the circle is: {area}")

circle1 = Circle(8)
circle1.get_area()
