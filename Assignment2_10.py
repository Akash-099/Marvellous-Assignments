#10.write program which accepts number from user and return addition of digits in that number
# input 5187934        Output 37

def num(n):

    temp = n
    sum = 0
    for i in str(temp):
        rem= temp%10
        sum +=rem
        temp=temp//10
        print(temp)
    print(sum)
        
        


def main():
    No = int(input("Enter No: "))
    res = num(No)
    print(res)

if __name__ == "__main__":
    main()