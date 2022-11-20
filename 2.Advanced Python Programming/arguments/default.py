
def area(Radius,Pi=3.14):#Default Arguments
    Result = Pi * Radius * Radius
    return Result

def main():
    Rvalue = 10.5 #Positional Arguments
    Pivalue = 3.14

#Positional arguments
    Ans = area(Rvalue,Pivalue) #Ans = Area(10.5,3.14)
    print("Area of circle is : ", Ans)

#Keyword arguments  
    Ans = area(Pi = Pivalue,Radius = Rvalue) #Ans = Area(10.5,3.14)
    print("Area of circle is : ", Ans)

#Positional arguments and second is default
    Ans = area(10.5)    #Default arguments
    print("Area of circle is : ",Ans) #Ans =Area(10.5)

#keyword arguments and second is default
    Ans = area(Radius=10.5)
    print("Area of circle is : ",Ans) #Ans =Area(10.5)

#Keyword arguments    
    Ans = area(Pi = 7.10, Radius=10.5)
    print("Area of circle is : ",Ans) #Ans =Area(10.5)

if __name__ == "__main__":
    main()  

    #Area of circle is 346.185 