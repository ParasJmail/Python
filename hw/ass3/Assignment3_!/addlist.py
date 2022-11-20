def Add(n):
    list1 = []
    for i in range(0,n):
        print("Enter the value")
        p = int(input())
        list1.append(p)
    print("Input Elements : ",list1)

    Sum = 0

    for j in range(0,len(list1)):
        Sum = Sum + list1[j]
    
    print("Output",Sum)