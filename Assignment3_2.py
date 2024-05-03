#write program which accepts N numbers from user and store it into list, return max number from that list.
# Input : Number of Elements: 5
#Input : Enter 5 List elements: [7,4,6,9,7]
#Output : 9


def max(lst):
    max = lst[0]
    for i in lst:
        if i> max:
            max = i
    return max


def main():
    size = int(input("Enter Size of List: "))
    arr = list()
    print("Enter List of ",size,"Elements")
    i = 0
    for i in range(0,size):
        no = int(input())
        arr.append(no)
    print(arr)

    res = max(arr)
    print("Max List Element is: ",res)
    


if __name__ == "__main__":
    main()

#Output
"""
C:\Users\Dhumal\Desktop\Python ML\Python_Assignments>python Assignment3_2.py
Enter Size of List: 7
Enter List of  7 Elements
13
5
45
7
4
56
34
[13, 5, 45, 7, 4, 56, 34]
Max List Element is:  56
"""