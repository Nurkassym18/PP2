def reversek(lst):
    for i in lst[::-1]:
        print(i)

words=[]
s=int(0)
while True:
    k=str(input())
    if k=="":
        break
    words.insert(s,k)
    s+=1
result = reversek(words)




    