#write a program which accepts two file names from user and compare contents of both the files if both the files contains same containts then display success otherwise display failure. accept names of both the files from command line.

#Input: Inputfile.txt  demo.txt
#compare contents of inputfile.txt and demo.txt


import os
import sys

def main():
    fname1= sys.argv[1]
    fname2= sys.argv[2]

    if os.path.exists(fname1) and os.path.exists(fname2):
        fobj = open(fname1,"r")
        cobj= open(fname2, "r")
        if fobj.read() == cobj.read():
            print("SuccessFul")
        else:
            print("Failure")
    else:
        print("Unable to open file,As it's Not Existing")

if __name__ == "__main__":
    main()