#Python operator
print(5+10)
x=15
y=5
print(int(x/y))
print(15%2) 
print(float(x-y))
print(x*y)
print(2**4) #power 

#Operators: And , or , not

k=int(input())
if k>=10 and k<=11:
    print("Yes")
else:
    print("NO")

if k==10 or k==11:
    print("Yes")
else:
    print("NO")
    
# is
lst=[1,2,3]
lst2=[1,2,3]
copy=lst
print(lst is lst2) #return false 
print(copy is lst) #return true
#in , not in 
num=1
print(num in lst) #return true
print(num not in lst) #return false


print(x&y) #and
print(x|y) #or
print(~x) #not
print(x^y) #Xor
print(x<<2) #shift to left 
print(x>>2) #shift to right