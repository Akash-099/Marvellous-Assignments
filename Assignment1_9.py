def even():
    count= 0
    number= 0

    while count <= 10:
        if number%2==0:
            count +=1
            print(number, end=" ")
        number+=1
        

            

        

def main():

    res = even()
    print(res)


if __name__ == "__main__":
    main()