from joueur import Joueur
from entraineur import Entraineur

class Equipe:
    def __init__(self, nom, entraineur):
        self.nom = nom
        self.entraineur = entraineur
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        # Point 5 : Ajouter le joueur si c'est un Joueur et si len < 11
        pass

    def __str__(self):
        return f"Equipe {self.nom} (Coach: {self.entraineur.nom}, {len(self.joueurs)} joueurs)"
