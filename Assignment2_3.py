#write a program which accept one number from user and return it's factorial.
#input = 5              Output= 120

def fact(a):
    if a<=0:
        res = print("Invalid Number, Enter +ve Number")
    else:
        i= 1
        fact= 1
        while i<=a:
            fact*=i
            res= fact
            i+=1
    return res



def main():
    No= int(input("Enter No: "))
    
    res = fact(No)
    print(res)

if __name__ == "__main__":
    main()
