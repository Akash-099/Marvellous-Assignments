def Star(a):
    for i in range(a):
        print("*", end=" ")

def main():
    no= int(input("Enter No: "))

    res= Star(no)

if __name__ == "__main__":
    main()