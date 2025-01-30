def filter_prime(number):
    count=int(0)
    for j in range(1,number+1):
        if number%j==0:
            count+=1

    if count==2:
        return True
    else: return False


lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
for i in range(len(lst)):
    nums = filter_prime(lst[i])
    if(nums==True):
       print(lst[i])