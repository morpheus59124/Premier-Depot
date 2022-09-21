def multiplication(n1, n2):
    """permet de multiplier deux nombres
    param :
        prend la valeur absolue du nombre
    return:
        multiplication"""
    if n1 < 0:
        n1 = -n1
    if n2 < 0:
        n2 = -n2
    return n1*n2

nb1 = int(input("Entrez un nombre "))
nb2 = int(input("Entrez un nombre "))
print (multiplication(nb1,nb2))