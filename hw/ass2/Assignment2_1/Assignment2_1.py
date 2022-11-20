from Arithmetic import *

def main():
    print("Enter No1 : ")
    No1 = int(input())

    print("Enter No2 : ")
    No2 = int(input())

    Sum = Add(No1,No2)
    
    minus = Sub(No1,No2)

    multi = Mult(No1, No2)

    Division = Div(No1,No2)

if __name__ == "__main__":
    main()