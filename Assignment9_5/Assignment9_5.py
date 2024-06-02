#Accept file name and one string from user and return the frequency of that string from file.
#input: Input.txt
#string: MArvellous
#search "Marvellous" in Input.txt

import os
import sys


def frequency(f,s):

    if os.path.exists(f):
        fobj = open(f, "r")
        text = fobj.read()
        
        
        print(text.casefold().count(s)) 

    else:
        print("Unable to open file,As it's Not Existing")

def main():
    fname= input("File Name: ")
    string = input("Enter string: ")
    
    frequency(fname, string.lower())


if __name__ == "__main__":
    main()