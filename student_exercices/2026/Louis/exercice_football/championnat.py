class Championnat:
    def __init__(self, nom, pays):
        self.nom = nom
        self.pays = pays
        self.equipes = []

    def inscrire_equipe(self, equipe):
        # Point 9 : Ajouter l'équipe à la liste
        pass

    def __str__(self):
        return f"{self.nom} ({self.pays}) - {len(self.equipes)} équipes engagées"
