lst = [1,2,3,4,5,6,7]
count=int(0)
prime_number=(lambda x:x>1 and all(x%i!=0  for i in range(2,x)))
prime_number1=list(filter(prime_number,lst))
print(prime_number1)