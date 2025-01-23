lst=[4,5,8,1,2,6,9,10]
#bubble sort 
for i in range(0,len(lst)-1):
    for j in range(len(lst)-1-i):
         if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)

#selection

for i in range(0,len(lst)-1):
    maxx=0
    for j in range(0,len(lst)-i):
        if lst[j]>maxx:
           maxx=j
    lst[len(lst)-1-i],lst[maxx]=lst[maxx],lst[len(lst)-1-i]

print(lst)