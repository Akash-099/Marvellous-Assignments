#Write a program which accepts N number from user and store it into list. Accept one another number from that list
#Input: Number of Elements: 5
#Input: Input Elements: [2,4,3,4,2]
#Input: Element To search : 4
#Output: 4 Element Found 2 Times in List

def frequency(lst, srch):
    count= 0
    for i in lst:
        if i == srch:
            count+=1
    return count 

    

def main():
    size = int(input("Enter Size of Elements: "))
    arr = list()
    print("Enter ", size, " List Elements")
    for i in range(size):
        no = int(input())
        arr.append(no)
    print(arr)
    search= int(input("Enter Element To Search: "))

    res = frequency(arr, search)
    print(search, "Element Found", res, " Times")

if __name__ == "__main__":
    main()


#Output
"""
C:\Users\Dhumal\Desktop\Python ML\Python_Assignments>python Assignment3_4.py
Enter Size of Elements: 11
Enter  11  List Elements
13
5
45
7
4
56
5
34
2
5
65
[13, 5, 45, 7, 4, 56, 5, 34, 2, 5, 65]
Enter Element To Search: 5
5 Element Found 3  Times
"""