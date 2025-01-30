def trueorfalse(lst):
    count=int(0)
    count1=int(0)
    for i in range(0,len(lst)):
        if lst[i]==0:
            count+=1
        elif lst[i]==7:
            count1+=1
        if count==2 and count1==1:
            return True
    return False
lsr1=[1,0,0,1,0]
res = trueorfalse(lsr1)
print(res)