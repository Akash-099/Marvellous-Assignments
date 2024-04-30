#write a program which accepts one number from user and display below pattern.
#input  5
"""
* * * * * 
* * * *
* * *
* *
*
"""

def star(a):
    temp = a
    for i in range(0,temp):
        print("\n")
        for i in range(0,temp):
            print("*", end=" ")
        temp-=1

def main():
    No= int(input("Enter No: "))
    res = star(No)

if __name__ == "__main__":
    main()