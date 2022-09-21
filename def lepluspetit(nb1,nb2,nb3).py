def lepluspetit(nb1,nb2,nb3):
    if nb1 < nb2 and nb1 < nb3:
        return nb1
    elif nb2 < nb1 and nb2 < nb3:
        return nb2
    elif nb3 < nb1 and nb3 < nb2:
        return nb3

nb1 = int(input("Entrez un nombre "))
nb2 = int(input("Entrez un nombre "))
nb3 = int(input("Entrez un nombre "))

print (lepluspetit(nb1,nb2,nb3))

