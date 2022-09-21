from tabnanny import NannyNag


dico = {}
dico = {
    "dictionnaire":"lexique des definitions des mots",
    "gaspard":"ok ta mere",
    "cannabis":"substance recreative"}
demande = input("Entrez un mot : ")
print(dico.get(demande,"Nous ne connaissons pas ce mot"))