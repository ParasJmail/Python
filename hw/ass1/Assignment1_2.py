def ChkNum():
    print("Enter Number : ")
    No = int(input())
    
    if No%2 == 0:
        print("Even Number")
    else: 
        print("Odd Number") 

if __name__ == "__main__":
    ChkNum()
