#write a program which accepts one number from user and check whether number is prime or not.
#input 5     Output = It is prime number
def prime(a):
    flag=0
    for i in range(2, a):
        if a%i==0:
            flag = 1
            break
    if flag==1:
        ret = "it is Not Prime Number"
    else:
        ret = "It is Prime Number"
    return ret


def main():
    No= int(input("Enter No to check It's Prime or Not: "))
    res = prime(No)
    print(res)

if __name__ == "__main__":
    main()