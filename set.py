#create a set 
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Set items are unordered, unchangeable, and do not allow duplicate values
#length
thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# method add 
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

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
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#discard
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#pop   remove random item 
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
# clear 
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
 #loop through set 
thisset = {"apple", "banana", "cherry"}

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
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#join by update 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#join by intersection 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) # return only 'apple'

#difference 
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)
 # symmetric - difference 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) #return banana cherry google microsoft