import os
import multiprocessing

def Square(No):
    print("PID of worker is {} for the input {}".format(os.getpid,No))
    return (No*No)

def main():
    print("Process ID of our application is : ",os.getpid())

    Data = [1,2,3,4,5]
    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(Square,Data)
    
    print("Result after square opearationis : ",Result)    

if __name__ == "__main__":
    main()    