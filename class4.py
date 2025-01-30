import math
class point:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    def show(self):
        return f"{self.x} {self.y}"
    def move(self):
        self.x=int(input())
        self.y=int(input())
        
    def dist(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
value = point(8,10)
value2 = point(3,4)
print(value.show())
print(value2.show())
value.move()
dstance=value.dist(value2)
print(dstance)