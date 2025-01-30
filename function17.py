def trueorfalse(lst):
    for i in range(1,len(lst)):
        if lst[i-1]==3 and lst[i]==3:
            return True
            break;
    return False
lsr1=[1,3,1]
res = trueorfalse(lsr1)
print(res)