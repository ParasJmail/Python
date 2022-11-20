Batches = {"PPA":18000 , "LB":16700, "Python":16500, "Angular":15000}

print("Data of Dictionary : ", Batches)

print("Data traversal using for loop")
for x in Batches:   #For displaying keys
    print(x)

print("Data traversal using for loop")
for x in Batches:   #For displaying keys and its values
    print(x,Batches[x])  #Fastest Way    

print("Data traversal using for loop")
for x in Batches:   #For displaying keys and its values
    print(x,Batches.get(x))  

keysBatches = Batches.keys()   #For showing only keys   
print(keysBatches)
print(type(keysBatches))

valuesBatches = Batches.values()   #For showing only keys   
print(valuesBatches)
print(type(valuesBatches))