from ast import Param


def est_pair (nb):
    """connaitre si le nombre est pair
    Param :
    nb nombre a determiner si pair ou impaire
    return :
    reste de la division different de 1
    """
    resultat = nb % 2 == 0
    return resultat

nb_user = int(input("Entrez un nombre entier : "))
print(est_pair(nb_user))
