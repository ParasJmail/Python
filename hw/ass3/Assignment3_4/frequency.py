def freq(n):
    list1 = []
    for i in range(0,n):
        print("Enter the value")
        p = int(input())
        list1.append(p)
    print("Input Elements : ",list1)

    fre = {}
    for items in list1:
        if (items in fre):
            fre[items] += 1
        else:
            fre[items] = 1

    for key, value in fre.items():
        print("%d : %d"%(key, value))

        
    
    