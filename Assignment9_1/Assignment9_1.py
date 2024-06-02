#write a program which accepts file name from user and check whether this file is existing in current directory or not

#Input: Input.txt
#check whether Input.txt file is existing in directory or not

import os
import sys
def finddirectory(Dname):
    flag = os.path.isabs(Dname)
    if flag==False:
       Dname= os.path.abspath(Dname)

    exist = os.path.isdir(Dname)
        
    if exist == True:
        print("Given Directory is Existing",Dname)
    else:
        print("No Such Directory ")


def main():
    if (len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Code is used to check file is existing in directory or not")
            exit()
        if (sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Usage of this Script is")
            print("File Name    Directory Name")
            exit()
        try:
            finddirectory(sys.argv[1])
        except Exception as obj1:
            print("Exception Occured due to ", obj1)

if __name__ == "__main__":
    main()