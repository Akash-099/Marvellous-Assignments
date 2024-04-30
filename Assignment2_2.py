#write a program which accepts one number and display below pattern.
#input 5
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

def Pattern(a):
    for i in range(0,a):
        print("\n")
        for i in range(0,a):
            print("*", end=" ")
    

def main():
    In= int(input("Enter Input: "))
    res = Pattern(In)

if __name__ == "__main__":
    main()