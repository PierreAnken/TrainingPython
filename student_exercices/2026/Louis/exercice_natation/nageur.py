class Nageur:
    def __init__(self, nom, temp_min):
        # Point 1 : Initialiser nom et temp_min
        # Vérifier que nom est une chaîne non nulle (ValueError sinon)

        self.nom = nom
        self.temp_min = temp_min

        if nom is None or type(nom) is not str:
            raise ValueError


    def __str__(self):
        # Point 2 : Retourner "Nageur [nom] (Min: [temp_min]°C)"

        return f"Nageur {self.nom} (Min: {self.temp_min}°C)"