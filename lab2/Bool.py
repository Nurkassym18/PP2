print(10 > 9) #true
print(10 == 9) #false
print(10 < 9) #false

#bool()
print(bool("My name is Nurkassym")) #true 
print(bool(18)) #true
print(bool(0)) #false

#bools which return false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
      return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Check if an object is an integer or not:
x = 200
print(isinstance(x, str)) #return false 
print(isinstance(x, int)) #return true