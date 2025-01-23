#create 
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#length of tuple
print(len(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#print second item
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#update 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#remove 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#unpacking tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)   #return apple,banana , [cherry, strawberry , raspberry]

#loop through tuple 
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


for i in range(len(thistuple)):
    print(thistuple[i])

#join 
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
