def main():

    no=int(input("Enter Input: "))
    #res= power(n)
    res = lambda no: (no**2)
    print(no, " Power Of 2 is: ",res(no))

if __name__ == "__main__":
    main()


#output

"""
C:\Users\Dhumal\Desktop\Python ML\Python_Assignments>python Assignment4_1.py
Enter Input: 12
12  Power Of 2 is:  144
"""