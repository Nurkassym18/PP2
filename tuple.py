#create 
thistuple = ("Kymyz", "shubat", "sut")
print(thistuple)
#length of tuple
print(len(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#print second item
thistuple = ("Kymyz", "shubat", "sut")
print(thistuple[1])

#update 
x = ("Kymyz", "shubat", "sut")
y = list(x)
y[1] = "Tary"
x = tuple(y)

print(x)

thistuple = ("Kymyz", "shubat", "sut")
y = list(thistuple)
y.append("Kurt")
thistuple = tuple(y)

#remove 
thistuple = ("Kymyz", "shubat", "sut")
y = list(thistuple)
y.remove("Kymyz")
thistuple = tuple(y)

#unpacking tuple
Nauryz = ("Kymyz", "shubat", "sut")

(green, yellow, red) = Nauryz

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)   #return apple,banana , [cherry, strawberry , raspberry]

#loop through tuple 
thistuple = ("Kymyz", "shubat", "sut")
for x in thistuple:
  print(x)


for i in range(len(thistuple)):
    print(thistuple[i])

#join 
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("Kymyz", "shubat", "sut")
mytuple = fruits * 2

print(mytuple)


Mytuple=("Name","Surname")
lst=["Nurkassym","tynystan"]
k=int(0)
sets=set({})
for i in range(len(Mytuple)):
    if Mytuple[i]=="Name":
        sss=Mytuple[i]+": "+lst[k]
        sets.add(sss)
        k+=1
    elif Mytuple[i]=="Surname":
        ssss=Mytuple[i]+": "+lst[k]
        sets.add(ssss)

lsttt=list(Mytuple)
lsttt.remove("Name")
Mytuple=tuple(lsttt)
print(Mytuple)
print(sets)
