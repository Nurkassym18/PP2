#create a set 
thisset = {18,19,true}
print(thisset)
#Set items are unordered, unchangeable, and do not allow duplicate values
#length
thisset = {1,2,"gfgf"}

print(len(thisset))


# method add 
thisset = {"Kymyz", "shubat", "sut"}

thisset.add("Kurt")

print(thisset)
# method update thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# add element from list to  a set 
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#remove 
thisset = {"Kymyz", "shubat", "sut"}

thisset.remove("shubat")

print(thisset)

#discard
thisset = {"Kymyz", "shubat", "sut"}

thisset.discard("Kurt")

print(thisset)
#pop   remove random item 
thisset = {"Kymyz", "shubat", "sut"}

x = thisset.pop()

print(x)

print(thisset)
# clear 
thisset = {"Kymyz", "shubat", "sut"}

thisset.clear()

print(thisset)
 #loop through set 
thisset = {"Kymyz", "shubat", "sut"}

for x in thisset:
  print(x)

#join by Union 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"Nurik", "Nuric"}
set4 = {"Kymyz", "shubat", "sut"}

myset = set1.union(set2, set3, set4)
print(myset)

#join by update 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#join by intersection 
set1 = {"Kymyz", "shubat", "apple"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) # return only 'apple'

#difference 
set1 = {"Kymyz", "shubat", "sut"}
set2 = {"google", "microsoft", "sut"}

set3 = set1.difference(set2)
print(set3)
 # symmetric - difference 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) #return banana cherry google microsoft