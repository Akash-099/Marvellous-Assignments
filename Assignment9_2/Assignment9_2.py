import os

def main():
    fname= input("Enter Name Of File Which you want to Open: ")

    
    if os.path.exists(fname):
        #fobj = open(fname, "x")
        sobj = open(fname,"r")
        Data = sobj.read()
        print(Data)
        sobj.close()
        
    else:
        print("Unable to open file,As it's Not Existing")

if __name__ == "__main__":
    main()