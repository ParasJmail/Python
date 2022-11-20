def factors(No):
    list = []
    for i in range(1,No):
        if No%i == 0:
            list.append(i) 
            i = i + 1
    print(list)

    iSum = 0
    for j in range(0,len(list)):
        iSum = iSum +list[j]

    print("sum of factors are : ",iSum)
    