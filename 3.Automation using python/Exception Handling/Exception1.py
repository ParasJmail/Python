

def main():
    print("Enter First Number")
    No1 = int(input())
    print("Enter Second Number")
    No2 = int(input())

    try:
        Ans = No1/No2
        print("Division is : ",Ans)

    except ZeroDivisionError:
        print("Exception Occured")    

        

if __name__ == "__main__":
    main()    