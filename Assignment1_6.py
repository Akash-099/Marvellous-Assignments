def Chknum(a):
    if a>0:
        i= "It's a Positive Number"
    elif a<0:
        i= "it's a Negative Number"
    else:
        i= "Zero"
    return i

def main():
    No= int(input("Enter Number: "))

    res= Chknum(No)

    print(res)

if __name__ == "__main__":
    main()