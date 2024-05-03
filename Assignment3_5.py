def main():
    size = int(input("Enter Size Of List"))
    arr= list()

    print("Enter", size, "list Elements")
    for i in range(0,size):
        no = int(input())
        arr.append(no)
    print("List is: ", arr)

if __name__ == "__main__":
    main()