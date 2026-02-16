from personne import Personne


class Joueur(Personne):
    def __init__(self, nom, age, poste, numero):
        # Point 3 : Appeler le constructeur parent et initialiser poste et numero
        super().__init__(self, nom, age)

    def __str__(self):
        # Point 3 : Surcharger pour afficher "Joueur [numero]: [nom] ([age] ans) - [poste]"
        # Indice : Utilisez super().__str__() pour la partie nom/age
        return ""
