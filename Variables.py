#python Variables
x = 18 #age 
y = "Nurkasym" #name
print(x)
print(y)


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 18 #age class 'int'
y = "Nurkasym" #name  class 'str'
print(type(x))
print(type(y))


#Variable names 
#legal variable names 
myvar = "Nurkasym"
my_var = "Nurkasym"
_my_var = "Nurkasym"
myVar = "Nurkasym"
MYVAR = "Nurkasym"
myvar2 = "Nurkasym"

#Assign Nultiple Values
x, y, z = "shabdaly", "Banana", "apple"
print(x)
print(y)
print(z)

x=y=z="shabdaly"
print(x,y,z)

#Unpack a list 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output variables 
x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

x = "Python"
y = "is"
z = "awesome"
print(x + y + z) #together 


#Global variables
x = "useful"

def myfunc():
  print("Python is " + x)

myfunc()
#second examples
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#third examples
def myfunc1():
      global x
  x = "fantastic"

myfunc()

print("Python is " + x)