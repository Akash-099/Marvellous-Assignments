#write a program which accepts one number and print below pattern.
"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""


def pattern(a):
     for i in range(0,a):
        print("\n")
        for i in range(1,a+1):
            print(i,end=" ")

def main():
    No = int(input("Enter Input: "))
    res = pattern(No)


if __name__ == "__main__":
    main()