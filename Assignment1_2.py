def Chknum(a):
    if a%2==0:
        chk= "Even Number"
    else:
        chk= "Odd Number"
    return chk



def main():
    No= int(input("Enter Number: "))
    ans= Chknum(No)
    print(ans)
if __name__=="__main__":
    main()