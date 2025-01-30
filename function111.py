def palindrome(word):
   return word==word[::-1] #compare word with reverse word


k=str(input())
Res=palindrome(k)
if(Res==True):
    print("Yes")
else:
    print("No")