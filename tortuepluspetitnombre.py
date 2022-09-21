nb1 = int(input("Entrez un nombre "))
nb2 = int(input("Entrez un nombre "))
nb3 = int(input("Entrez un nombre "))

if nb1 < nb2 and nb1 < nb3:
    print(str(nb1)+ "est plus petit")
elif nb2 < nb1 and nb2 < nb3:
    print(str(nb2)+ "est plus petit")
elif nb3 < nb1 and nb3 < nb2:
    print(str(nb3)+ "est plus petit")
