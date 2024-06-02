#write program which accepts file name from user and create new file names as inputfile.txt and copy all contents from existing file into new file. acceptfile name through command line arguments.

#Input: Inputfile.txt
#create new file as demo.txt and copy contents of inputfile.txt in demo.txt

import sys
import os

def main():
    fname = sys.argv[1]
    demo = sys.argv[2]
    if os.path.exists(fname):
        fobj = open(fname,"r")
        data = fobj.read()
        sobj = open(demo,"x")
        sobj.write(data)
        sobj.close()
        aobj = open(demo, "r")
        Data = aobj.read()
        print(Data)
        fobj.close()
        aobj.close()
    else:
        print("Unable to open file,As it's Not Existing")

if __name__ == "__main__":
    main()