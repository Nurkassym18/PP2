a = 33
b = 33
if b > a:
  print("Yes,it is true")
elif a == b:
  print("a and b have the same value")


  a = 200
b = 33
if b > a:
  print("")
elif a == b:
  print("Yes,it is true")
else:
  print("b is smaller  number than a ")

  #both conditions 
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both statements are satisfyied")



a = 200
b = 33
c = 500
if a > b or a > c:
  print("one true , one false ")


a = 33
b = 200
if not a > b:
  print("Yes")


# if in if 
x = 41

if x > 10:
  print("greater than ten ")
  if x > 20:
    print("and also greater than twenty")
  else:
    print("but not above 20.")
