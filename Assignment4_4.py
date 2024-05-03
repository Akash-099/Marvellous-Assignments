from functools import reduce

def main():
    size = int(input("Enter Size of List: "))
    arr = list()

    print("Enter Elements in list: ")
    for i in range(0, size):
        no = int(input())
        arr.append(no)
    print("List Is: \n", arr)

    chkeven = list(filter(lambda no: no%2==0, arr))
    print("Data after filtering Even number is: \n", chkeven)

    square = list(map(lambda no : no^2,chkeven))
    print("Data after mapping even numbers square is \n", square)

    add = reduce(lambda a,b : a+b, square)
    print("Data After addition of Even Number's square's addition \n",add)

if __name__ == "__main__":
    main()\
    

#output

"""
C:\Users\Dhumal\Desktop\Python ML\Python_Assignments>python Assignment4_4.py
Enter Size of List: 10
Enter Elements in list:
5
2
3
4
3
4
1
2
8
10
List Is:
 [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
Data after filtering Even number is:
 [2, 4, 4, 2, 8, 10]
Data after mapping even numbers square is
 [0, 6, 6, 0, 10, 8]
Data After addition of Even Number's square's addition
 30

"""