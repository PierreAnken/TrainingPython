# Exercice 1.b (expressions conditionnelles)
a = int(input("Entrez l’âge du joueur : "))
if a < 8:
    print("Le joueur est trop jeune")
elif 8 <= a < 10:
    print("Le joueur est dans la catégorie U10")
elif 10 <= a < 12:
    print("Le joueur est dans la catégorie U12")
elif 12 <= a < 14:
    print("Le joueur est dans la catégorie U14")
elif 14 <= a < 16:
    print("Le joueur est dans la catégorie U16")
