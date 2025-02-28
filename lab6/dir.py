#1
import os
def checking(path):
    directories = []  
    files = []  
    for i in os.listdir(path):
        item_path = os.path.join(path, i) 

        if os.path.isdir(item_path):
            directories.append(i)  
        else:
            files.append(i) 

    print('\n'.join(directories))

    print('\n'.join(files))

    print('\n'.join(os.listdir(path)))

path = input()

checking(path)
#2 
import os 
def check_path(path):
    if os.path.exists(path):
        print("path is exist")

        if os.access(path,os.R_OK):
            print("Path is readibility ")
        else :
            print("Path is not readibility ")
        

        if os.access(path,os.W_OK):
            print("Path is writability")
        else :
            print("Path is not writability")

        if os.access(path,os.X_OK):
            print("Path is executability")
        else :
            print("Path is not executability")
        
    else :
        print("Path is not exist")
path = input()
check_path(path)

#3
def check_path_file(Path):
    if os.path.exists(Path):
        print("Path is exists")

        filname = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Filename is {filname} ")
        print(f"Directory is {directory} ")
    else :
        print("Path is not exist")

Path = input()
check_path_file(Path)
#4
file = open("112.txt","r")
count_row = 0
for row in file:
    count_row = count_row + 1
print(count_row)
file.seek(0)
count_row2=sum(1 for row in file  )
print(count_row2)
#5
Mylist = ["Hello","Hi"]
with open("list.txt","w") as file:
    for i in Mylist:
        file.write(i + "\n")
#6 
for i in range(1,27):
    with open(f"{chr(64+i)}.txt", "w") as file:
        file.write("hello ")
#7 
def copy():
    try:
        with open("111.txt","r") as first_file:
            content = first_file.read()
        
        with open("112.txt","w") as second_file:
            second_file.write(content)
    
    except Exception as e:
        print(f"Error:{e}")
copy()

with open("112.txt","r") as second_files:
    print(second_files.read())

#8 
def delete_path(Path):
    try:
        if os.path.exists(Path):

            if os.access(Path,os.R_OK) and os.access(Path,os.W_OK):
                os.remove(path)

            else :
                print("Path is not accessible")

        else :
            print("Path does not exist")

    except Exception as e:
        print(f"Error:{e}")

Path = input()
delete_path(Path)

