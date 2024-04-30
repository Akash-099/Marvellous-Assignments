#Write a program which accept number from user and return number of digits in that
#input    5187934             Output: 7


def num(n):

    temp = n
    count = 0
    for i in str(temp):
        temp= temp//10
        count+=1
    print(count)
        
        


def main():
    No = int(input("Enter No: "))
    res = num(No)
    print(res)

if __name__ == "__main__":
    main()