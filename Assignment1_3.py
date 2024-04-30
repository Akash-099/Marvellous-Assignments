def Add(a,b):
    return a+b
    

def main():
    No1= int(input("Enter First Number : "))
    No2= int(input("Enter Second Number: "))

    result = Add(No1,No2)
    print("Addition Is ", result)

if __name__ == "__main__":
    main()