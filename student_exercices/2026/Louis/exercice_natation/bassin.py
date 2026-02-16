from ligne_de_nage import LigneDeNage

class Bassin:
    def __init__(self, nom, temperature):
        # Point 6 : Initialiser nom, temperature et une liste vide 'lignes'

        self.nom = nom
        self.temperature = temperature
        self.lignes = []

    def ajouter_ligne(self, ligne):
        # Point 7 : Ajouter une ligne au bassin
        # Vérifier que 'ligne' est bien une instance de LigneDeNage

        if isinstance(ligne, LigneDeNage):
            pass

        self.lignes.append(ligne)