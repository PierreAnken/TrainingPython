from nageur import Nageur

class LigneDeNage:
    def __init__(self, numero):
        # Point 3 : Initialiser numero et une liste vide 'nageurs'

        self.numero = numero
        self.nageurs = []

    def ajouter_nageur(self, nageur):
        # Point 4 : Ajouter le nageur si len < 2, sinon ne rien faire
        # Vérifier que 'nageur' est bien une instance de Nageur
        if isinstance(nageur, Nageur) and len(self.nageurs) < 2:
            self.nageurs.append(nageur)



    def __len__(self):
        # Point 5 : Retourner le nombre de nageurs
        return len(self.nageurs)
