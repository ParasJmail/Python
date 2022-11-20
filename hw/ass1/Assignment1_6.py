def main():
    print("Enter Number : ")
    No = int(input())

    if No >> 0:
        print("Positive Number")
    elif No == 0:
        print("zero")
    else:
       print("Negative Number")  

if __name__ == "__main__":
    main()