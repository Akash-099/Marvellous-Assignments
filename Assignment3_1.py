"""Write a program which accept N numbers from user and storre it into list. 
Return addition of all element from that list. 
Input: Number elements: 6
Input Elements: 13  5   45  7   4 56
oUTPUT: 130
"""

def lst(a,b):
    print("Enter List Elements: ")
    for i in range(0,b):
        No= int(input())
        a.append(No)
    return a

def add(arr):
    sum = 0
    for i in arr:
        sum=sum+i
    return sum
    


def main():
    size= int(input("Enter Size of List: "))
    arr = list()
    res = lst(arr,size)
    print(res)
    result = add(res)
    print(result, "Is the addition of all list elements")    
if __name__ == "__main__":
    main()


#OUTPUT
"""
C:\Users\Dhumal\Desktop\Python ML\Python_Assignments>python Assignment3_1.py
Enter Size of List: 4
Enter List Elements:
1
2
3
4
[1, 2, 3, 4]
10 Is the addition of all list elements
"""
