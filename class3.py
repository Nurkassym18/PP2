class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__ (self,length):
        self.length = length
    def area(self):
        return self.length*self.length
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

rectangle=Rectangle(5,12)
squares =Square(22)
shapes = Shape()
print(squares.area())
print(shapes.area())
print(rectangle.area())
    