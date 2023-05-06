import random


# Valeurs des lettres Scrabble
valeurs_lettres = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

# Distribution des lettres Scrabble
distribution_lettres = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9,
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6,
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}

# Créer un ensemble de tuiles de lettres
tuiles_lettres = []
for lettre, compte in distribution_lettres.items():
    tuiles_lettres += [lettre] * compte
    random.shuffle(tuiles_lettres)

# Boucle principale du jeu
score_joueur_1 = 2
score_joueur_2 = 0
while tuiles_lettres:

    # Piocher des tuiles pour les deux joueurs
    tuiles_joueur_1 = [tuiles_lettres.pop() for _ in range(7)]
    tuiles_joueur_2 = [tuiles_lettres.pop() for _ in range(7)]

    print(f'Tuiles joueur 1: {tuiles_joueur_1}')
    print(f'Tuiles joueur 2: {tuiles_joueur_2}')

    # Obtenir le mot et le score du joueur 1
    mot_joueur_1 = input('Joueur 1, entrez un mot: ').upper()
    score_joueur_1 += sum(valeurs_lettres[lettre] for lettre in mot_joueur_1)
    print(f'Score joueur 1: {score_joueur_1}')

    # Obtenir le mot et le score du joueur 2
    mot_joueur_2 = input('Joueur 2, entrez un mot: ').upper()
    score_joueur_2 += sum(valeurs_lettres[lettre] for lettre in mot_joueur_2)
    print(f'Score joueur 2: {score_joueur_2}')
