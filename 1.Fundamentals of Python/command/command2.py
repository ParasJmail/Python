import sys

def Addition(A,B):
    Ans = 0
    Ans = A + B
    return Ans

def main():
    print("Welcome to : ", sys.argv[0])
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] =="--U"):
            print("Use the application as :")
            print("python Name_of_Application First_number Second_number")
            exit()

        if(sys.argv[1] =="--H"):
            print("Help :This application is used to perform addition of 2 numbers")
            exit()


    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Please use --U flag to get the usage")
        exit()

    Ret = Addition(int(sys.argv[1]),int(sys.argv[2]))
    
    print("Addition is : ",Ret)   

    print("Thank you for using the application")
    print("By Paras Jaitly")

if __name__ == "__main__":
    main()   