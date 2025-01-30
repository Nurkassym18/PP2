def unique(lst):
    lst2=[]
    for i in range(len(lst)):
        if lst[i] in lst2:
            continue
        else:
            lst2.append(lst[i])

    return lst2
lst1=[1,2,2,3,3,4]
res=unique(lst1)
print(res)