#task1
from functools import reduce
from operator import mul
MYList =[1,2,3,4,5]
def all_mul(MYList):
    res =reduce(mul,MYList)
    return res
print(all_mul(MYList))

#task2
text="TynystanNurkasym"
cnt = sum(1 for i in text if i.islower() )
cnt1 = sum(1 for i in text if i.isupper() )
print(f"lower: {cnt} \nupper: {cnt1}")

#task3
text1="madam"
g = reversed(text1)
res = "".join(g)
if res == text1:
    print("yeeeep")
else:
    print("cryyy")

#task4
import time
import math
b = int(input())
a = int(input())
time.sleep(a//1000)
print(math.sqrt(b))

#task5
def all_true(Mytuple):
    return all(Mytuple)

Mytuple=(1,"adshjl")
print(all_true(Mytuple))
