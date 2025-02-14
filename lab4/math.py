import math 
#1
x = int(input())
y =math.radians(x)
print(y)

#2 
H=int(input("Height:"))
S=int(input("Base, first value:"))
S1=int(input("Base, second value:"))
Area = ((S+S1)/2)*H
print(f"Expected Output: {Area}")

#3
x=int(input("Input number of sides:"))
y= int(input("Input the length of a side:"))
perimetr = x*y
apothem = y/(2*math.tan(math.radians(180/x)))
Area = (perimetr*apothem)/2
print(Area)

#4
L=int(input("Length of base:"))
H=int(input("Height of parallelogram:"))
print(float(L*H))