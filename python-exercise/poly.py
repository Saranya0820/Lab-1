import math

class shapes:
    def area(self):
        pass

    def perimeter(self):
        pass


class circle(shapes):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return math.pi*self.radius**2

    def perimeter(self):
        
        return 2 * math.pi * self.radius

class Rectangle(shapes):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 *(self.length + self.width)
    

class Triangle(shapes):
    def __init__(self,a,b,c,h):
       self.a = a
       self.b = b
       self.c = c
       self.h = h

    def area (self):
        return 0.5 * self.b * self.h
    def perimeter(self):
        return self.a +self.b +self.c

cir = circle(5)
print("Area of Circle: ")
print(cir.area())
print("Perimeter of Circle: ")
print(cir.perimeter())

Rect = Rectangle(10,20)
print("Area of Rectangle:")
print(Rect.area())
print("Perimeter of Rectangle:")
print(Rect.perimeter())