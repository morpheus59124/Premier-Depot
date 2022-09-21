"""permet de faire une boucle en rajoutant un # a chaque ligne supp
variable:
    variable vide 
"""
nb1 = int(input("Entrez un nombre "))
variable = ""
"""for:
    boucle du nbre de fois ou il ajoute en # 
    variable:
    ajoute un # tant que la boucle n est pas termine"""
for i in range(nb1):
    variable += "#"
    print(variable)
