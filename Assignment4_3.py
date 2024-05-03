from functools import reduce

def main():
    size = int(input("Size Of List: "))
    arr = list()
    print("Enter Elements In List: ")
    for i in range (0,size):
        no = int(input())
        arr.append(no)
    print(arr)


    chknum= list(filter(lambda no : no>=70, arr))
    print("Data from filtered List: ",chknum)

    increse = list(map(lambda no : no+10, chknum))
    print("Data After Incresing No by 10: ", increse)

    product = reduce(lambda a,b : a*b, increse)
    print("Product of All Mapped list is: ", product)



if __name__ == "__main__":
    main()


#Output

"""
C:\Users\Dhumal\Desktop\Python ML\Python_Assignments>python Assignment4_3.py
Size Of List: 12
Enter Elements In List:
4
34
36
76
68
24
89
23
86
90
45
70
[4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
Data from filtered List:  [76, 89, 86, 90, 70]
Data After Incresing No by 10:  [86, 99, 96, 100, 80]
Product of All Mapped list is:  6538752000

C:\Users\Dhumal\Desktop\Python ML\Python_Assignments>
"""

