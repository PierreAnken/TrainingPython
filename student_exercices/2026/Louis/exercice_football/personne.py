class Personne:
    def __init__(self, nom, age):
        # Point 1 : Initialiser nom et age
        self.nom = nom
        self.age = age

    def __str__(self):
        # Point 2 : Retourner "[nom] ([age] ans)"
        return f"{self.nom} ({self.age} ans)"
