#change items
lst=[1,2,3,4]
lst[2]=6
print(lst)
 
thislist = [1,2,3,4,5,6,7,8,9]
thislist[1:3] = [54,45]
print(thislist)

#type of a list 
mylist = ["Kymyz", "shubat", "sut"]
print(type(mylist))

thislist = ["Kymyz", "shubat", "sut"]
print(thislist[1]) 
thislist = ["Kymyz", "shubat", "sut"]
print(thislist[-1]) 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) 

#in 
thislist = ["Kymyz", "shubat", "sut"]
if "sut" in thislist:
  print("Yes, 'apple' is in the fruits list")

#insert 
thislist = ["Kymyz", "shubat", "sut"]
thislist.insert(2, "Kurt")
print(thislist) #return "Kymyz", "shubat","kurt", "sut"

#append
thislist = ["Kymyz", "shubat", "sut"]
thislist.append("Kurt")
print(thislist) #return "Kymyz", "shubat", "sut","kurt"

#extend
lst=[1,2,3]
lst2=[4,5,6]
lst.extend(lst2)
print(lst) # 1,2,3,4,5,6

#remove
thislist = ["Kymyz", "shubat", "sut"]
thislist.remove("Kymyz")
print(thislist) 

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) 

#pop()
thislist = ["Kymyz", "shubat", "sut"]
thislist.pop()
print(thislist)

thislist = ["Kymyz", "shubat", "sut"]
thislist.pop(1)
print(thislist) 

# delete 
thislist = ["Kymyz", "shubat", "sut"]
del thislist[0]
print(thislist) #return shubat  sut

#clear
thislist = ["Kymyz", "shubat", "sut"]
thislist.clear()
print(thislist) #return [] delete all 

#loop through a list 
thislist = ["Kymyz", "shubat", "sut"]
for x in thislist:
    if x=="sut":
       print(x)
#by range and While
thislist = ["Kymyz", "shubat", "sut"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["Kymyz", "shubat", "sut"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#short hand for loop
thislist = ["Kymyz", "shubat", "sut"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 


#sort list 
thislist = ["Kymyz", "shubat", "sut"]
thislist.sort()
print(thislist)
#reverse sort
thislist = [1,2,3,4,5,6,7,8,9,7]
thislist.sort(reverse = True)
print(thislist)

#reverse 
thislist = ["Kymyz", "shubat", "sut"]
thislist.reverse()
print(thislist)

#copy 
thislist = ["Kymyz", "shubat", "sut"]
mylist = thislist.copy()
print(mylist)

thislist = ["Kymyz", "shubat", "sut"]
mylist = list(thislist)
print(mylist) #list method

#join two list 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)