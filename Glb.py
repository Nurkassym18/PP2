x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


# second 
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



# Python is fantastic
def myfunc():
      global x
  x = "fantastic"

myfunc()

print("Python is " + x)