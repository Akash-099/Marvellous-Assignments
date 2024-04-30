def div(a):
    if a%5==0:
        i = True
    else:
        i = False
    return i

def main():
    no = int(input("Enter Number: "))

    res = div(no)
    print(res)

if __name__ == "__main__":
    main()