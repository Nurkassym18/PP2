#1
def square(A):
    for i in range(1,A+1):
        yield i*i
A=int(input())
for x in square(A):
    print(x)

#2
def even_number(B):
    for i in range(0,B+1):
        if i%2==0:
            yield i

B = int(input())
for x in even_number(B):
    print(x)

#3
def divisible_by(A):
    for i in range(1,A+1):
        if i%3==0 and i%4==0:
            yield i 
A=int(input())
for x in divisible_by(A):
    print(x)

#4
def square2(A,B):
    for i in range(A,B+1):
        yield i*i

A=int(input())
B=int(input())
for x in square2(A,B):
    print(x)


#5
def all_numbers(A):
    for i in range(0,A+1):
        yield i
A=int(input())
for x in all_numbers(A):
    print(x)
