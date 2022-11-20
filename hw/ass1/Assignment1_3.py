def Add(x,y):
    Result = x + y
    return Result

def main():
    print("Enter First Number : ")
    no1 = int(input())
    print("Enter Second Number : ")
    no2 = int(input())

    Sum = Add(no1,no2)

    print("Addition is : ",Sum)

if __name__ == "__main__":
    main()        