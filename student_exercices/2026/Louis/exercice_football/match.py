from arbitre import Arbitre

class Match:
    def __init__(self, equipe_domicile, equipe_exterieur, arbitre):
        self.equipe_domicile = equipe_domicile
        self.equipe_exterieur = equipe_exterieur
        self.arbitre = arbitre
        self.score = (0, 0)
        self.termine = False

    def marquer_but(self, est_domicile):
        # Point 6 : Incrémenter le score (domicile ou extérieur)
        pass

    @staticmethod
    def duree_reglementaire():
        # Point 7 : Retourner 90
        return 0

    def __str__(self):
        status = "Terminé" if self.termine else "En cours"
        return f"{self.equipe_domicile.nom} {self.score[0]} - {self.score[1]} {self.equipe_exterieur.nom} ({status})"
