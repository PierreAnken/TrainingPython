from nageur import Nageur
from bassin import Bassin


class Piscine:
    def __init__(self, nom):
        # Point 8 : Initialiser nom, ouverte (False) et une liste vide 'bassins'
        self.nom = nom
        self.ouverte = False
        self.bassins = []

    def ouvrir(self):
        # Point 9 : Passer ouverte à True
        self.ouverte = True

    def entrer(self, nageur:Nageur, bassin:Bassin):
        # NOUVEAU : Vérifier les types de 'nageur' et 'bassin'.
        if type(nageur) is Nageur and type(bassin) is Bassin:

            # Point 10 : Vérifier si la piscine est ouverte,
            if self.ouverte:

                # si la température du bassin >= nageur.temp_min,
                if bassin.temperature >= nageur.temp_min:

                    # et s'il y a de la place dans une des lignes du bassin.
                    for ligne in bassin.lignes:
                        if len(ligne) < 2:
                            # Si le nageur entre, l'ajouter physiquement à la ligne de nage.
                            ligne.ajouter_nageur(nageur)
                            return True

                # Retourner True si le nageur est entré, False sinon.

        return False
