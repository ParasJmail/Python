#Accept 2 numbers and perform addition and substraction of it

#Kya karna hain --> Behaviour(Function)
#Addition and Substaction

#Vo karne ke liye kya lagne vala hain --> Characteristics(Data)
#2 numbers

#Class = Characteristics +Behaviour
#Class = Data + Function

    
class Arithematic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Add(self):
            return self.No1+self.No2
   
    def Sub(self):
            return self.No1-self.No2

def main():
    print("Enter First Number")
    Value1 = int(input())

    print("Enter Second Number")
    Value2 = int(input())

    obj = Arithematic(Value1,Value2)

    Ans = obj.Add()
    print("Addition is : ",Ans)

    Ans = obj.Sub()
    print("Substraction is : ",Ans)

if __name__ == "__main__":
    main()    