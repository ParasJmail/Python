from sys import *

def fun(No):
    if((No % 2) == 0):
            print("It is even number")
    else:
        print("It is odd number")

def main():
    print("applicatin name : " +argv[0])

    if(len(argv)!= 3):
        print("Error : Invalid number of arguments")
        exit()    
    if argv[1] == "-h":
        print("The script is designed for_____________")   


if __name__ == "__main__":
    main()



    #HALF DONE ONLY