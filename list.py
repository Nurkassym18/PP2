#change items
lst=["apple","banana","cherry"]
lst[2]="watermelon"
print(lst)
 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#type of a list 
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #return banana
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #return cherry
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #return cherry , orange , kiwi

#in 
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#insert 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #return apple banana watermelon cherry

#append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #return apple banana cherry orange

#extend
lst=[1,2,3]
lst2=[4,5,6]
lst.extend(lst2)
print(lst) # 1,2,3,4,5,6

#remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # return apple , cherry

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #return apple , cherry,banana,kiwi

#pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #return apple , banana

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #return apple , cherry

# delete 
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #return banana, cherry 

#clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #return [] delete all 

#loop through a list 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    if x=="banana":
       print(x)
#by range and While
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#short hand for loop
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 


#sort list 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#reverse sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#reverse 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#copy 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) #list method

#join two list 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)