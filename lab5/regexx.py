#1

import re 
txt = "aabbbbc"
x=re.search("ab*?",txt)
if x :
    print("Yes")
else :
    print("No")

#2
txt2="abbc"
x2=re.search("ab{2,3}?",txt2)
if x2 :
    print("Yes")
else :
    print("No")

#3 
def myfunction(txt3):
    if  re.search('^[a-z]+_[a-z]+$',txt3):
        return "Found a match"
    else :
        return "Not found"

txt3="nuric_nefk"
print(myfunction(txt3))
#4 
def myfunc(txt4):
    if re.search('^[A-Z][a-z]+$',txt4):
        return "Match Found"
    else:
        return "Not Found"
txt4="Nuric"
print(myfunc(txt4))
#5
def myfunction1(txt5):
    if re.search('a.*b$',txt5):
        return "Found a match"
    else : 
        return "Not Found"
print(myfunction1("abvcsvdbbb"))

#6
def myfunction2(txt6):
    pattern=r'[ ,.]'
    result = re.sub(pattern,":",txt6)
    return result
print(myfunction2("Nuric_N K."))
#7
txt="Nurik_hgfs"
result = re.sub(r'_([a-z]){1}',lambda match:match.group(1).upper(),txt)
print(result)
#8
def splits(txt8):
    pattern=r'(?=[A-Z])'
    result=re.split(pattern,txt8)
    return result
print(splits("NurkasymTynystan"))

#9
import re
def otherwise(txt9):
    pattern=r'(?=[A-Z])'
    result=re.sub(pattern," ",txt9)
    return result
print(otherwise("NurkasumTynystan"))

#10 
def camel_to_snace(txt10):
    result=re.sub(r'(?=[A-Z])',"_",txt10)
    return result
print(camel_to_snace("NurkasymTynystan"))


#10 another variant
txt11 = "TynystanNurkasym"
res = re.sub(r'([A-Z]){1}', lambda match: "_" + match.group(1).lower(), txt11).lstrip('_')
print(res)

