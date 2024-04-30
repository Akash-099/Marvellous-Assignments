#Write a program which accepts one number and display below pattern.
#Input 5
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""


def pattern(n):
    for i in range(0,n):
        print("\n")
        num=1
        for j in range(0, i+1):
            print(num, end=" ")
            num+=1

def main():
    No = int(input("Enter Input: "))
    pattern(No)

if __name__ == "__main__":
    main()