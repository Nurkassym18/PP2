thisdict = {
  "Name": "Nurkassym",
  "Surname": "Tynystan",
  "Age": 18
}

#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

thisdict = {
  "Name": "Nurkassym",
  "Surname": "Tynystan",
  "Age": 18
}
print(thisdict["brand"])#return "Ford"

thisdict = {
"Name": "Nurkassym",
  "Surname": "Tynystan",
  "Age": 18
  "parents:": ["Kalyk", "Gulvira"]#list in value 
}

#use dict method
thisdict = dict(name = "Nurkasym", age = 18, country = "Kazakhstan")
print(thisdict)


#get 
thisdict =	{
  "Name": "Nurkassym",
  "Surname": "Tynystan",
  "Age": 18
}
x = thisdict.get("Age")
print(x)

#keys
thisdict = {
 "Name": "Nurkassym",
  "Surname": "Tynystan",
  "Age": 18
}

x = thisdict.keys()

print(x)
#values 
kl=thisdict.values()
print(kl)
#items 
rf=thisdict.items()
print(rf)

# update
thisdict = {
  "Name": "Nurkassym",
  "Surname": "Tynystan",
  "Age": 18
}
thisdict.update({"Age": 19})

#add new elements 
thisdict = {
 "Name": "Nurkassym",
  "Surname": "Tynystan",
  "Age": 18
thisdict.update({"height": "178"})

# remove by popitem()
thisdict = {
  "Name": "Nurkassym",
  "Surname": "Tynystan",
  "Age": 18
}
thisdict.popitem()
print(thisdict)
#clear 
thisdict = {
 "Name": "Nurkassym",
  "Surname": "Tynystan",
  "Age": 18
}
thisdict.clear()
print(thisdict)
#pop
thisdict = {
  "Name": "Nurkassym",
  "Surname": "Tynystan",
  "Age": 18
}
thisdict.pop("Age")
print(thisdict)

#loop 
for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x, y in thisdict.items():
  print(x, y)


  #copy 
thisdict = {
  "Name": "Nurkassym",
  "Surname": "Tynystan",
  "Age": 18
}
mydict = thisdict.copy()
print(mydict)


thisdict = {
  "Name": "Nurkassym",
  "Surname": "Tynystan",
  "Age": 18
}
}
mydict = dict(thisdict)
print(mydict)

#nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Nurkasym",
    "year" : 2006
  },
  "child2" : {
    "name" : "Adiya",
    "year" : 2006
  }
}

print(myfamily["child1"]["name"])


for x, obj in myfamily.items():
      print(x)

  for y in obj:
    print(y + ':', obj[y])