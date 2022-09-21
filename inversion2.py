from tokenize import Number


numbers=[1, "test", 0.9867, "Python, c'est génial !"]
print(numbers)
def listinverse(liste):
    listevide = []
    for elem in liste:
        listevide.insert(0,elem)
    return listevide
print (listinverse(numbers))      
