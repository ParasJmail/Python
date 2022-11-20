def prime(No):
    for i in range(2,int(No/2)+1):
        if (No%i) == 0:
            print(No,"is not a prime number")
            break
        else:
            print(No,"is a prime number")
            break