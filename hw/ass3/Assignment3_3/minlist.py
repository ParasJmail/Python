def Minimum(n):
    list1 = []
    for i in range(0,n):
        print("Enter the value")
        p = int(input())
        list1.append(p)
    print("Input Elements : ",list1)

    Answer = min(list1)
    
    print("Output",Answer)