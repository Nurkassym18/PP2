class shape:
    def area(self):
        return 0
class square(shape):
    def __init__ (self,length):
        self.length = length
    def area(self):
        return self.length*self.length

squares =square(22)
shapes = shape()
print(squares.area())
print(shapes.area())
    