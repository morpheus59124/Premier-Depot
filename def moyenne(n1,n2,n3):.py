def moyenne(n1,n2,n3):
    """permet de calculer la moyenne de 3 nombres
    Param :
    nb1,nb2,nb3 sont les nombres donnes par l utilisateur
    return :
    permet de faire la moyenne des 3 en les divisant par 3
    """   
    resultat = n1+n2+n3
    resultat = resultat /3 
    return resultat

nb1 = int(input("Entrez un nombre "))
nb2 = int(input("Entrez un nombre "))
nb3 = int(input("Entrez un nombre "))


print (moyenne(nb1,nb2,nb3))