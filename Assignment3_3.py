#Write a program which accepts N numbers from user and store it in list. return Minimum number from list.
#Input :Enter size of list: 3
#Input Elements: [20,1,44]
#Output: Min = 1


def min(lst):
    min= lst[0]
    for i in lst:
        if i<min:
            min=i
    return min

def main():
    size = int(input("Enter Size Of List: "))
    arr= list()
    print("Enter ", size, "Elements")
    for i in range(0, size):
        no = int(input())
        arr.append(no)
    print(arr)

    res = min(arr)
    print("Minimum Number From", arr , " is ",res)


if __name__ == "__main__":
    main()

#Output
"""
C:\Users\Dhumal\Desktop\Python ML\Python_Assignments>python Assignment3_3.py
Enter Size Of List: 4
Enter  4 Elements
13
5
45
7
[13, 5, 45, 7]
Minimum Number From [13, 5, 45, 7]  is  5

"""