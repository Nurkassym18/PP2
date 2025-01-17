#Python Strings
print("Hello")
print('Hello')

#we can use three double  quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#loop 
for x in "banana":
  print(x)    # b a n a n a


#length
a = "Hello, World!"
print(len(a))

#check class 'bool'
txt = "The best things in life are free!"
print("free" in txt) #return true

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


  #slicing 
b = "Hello, World!"
print(b[2:5]) # llo

b = "Hello, World!"
print(b[:5])
b = "Hello, World!"
print(b[-5:-2]) # начинает с конца 

#Modify String

a="KAZAKSTAN"
print(a.lower())
A='kazakhstan'
print(A.upper())

A="Almaty 05"
print(A.strip())
print(A.replace("l","a")) #Aamaty
print(A.split(" ")) #['Almaty' , '05']

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

x=10
print(f"I have {x:.2f} dollars") #10.00

#\n - new line

A="aBBBaaBB"
print(A.count("B"))
print(A.capitalize())
print(A.find('B')+1)
print(A.rfind("B"))
print(A.translate("B"))
print(A.partition("a"))