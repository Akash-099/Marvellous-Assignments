
def main():
    size= int(input("Enter Size of List: "))
    arr = list()
    print("Enter List Elements: ")
    for i in range(0,size):
        arr.append(i)
    print(arr)

    if __name__ == "__main__":
        main()