"""
1. Créer un range de 1 à 100:
2. Définit un chiffre avec entre 0 et 100 de façon alétoire
3. demander à l'utilisateur de deviner le numéro
4. si le num. est au dessus de chiffre à trouver msg -> tu es au dessus
5. idem 4 si en dessous
6. fait une boucle et jusqu'à que le chiffre à trouver soit deviné
7. bravo

"""

import random

chiffre_a_deviner = random.randint(1, 100)
response = ''
vies = 7

while response != chiffre_a_deviner and vies > 0:
    response = ''

    while not response.isdigit():
        response = input(f"Deviner le chiffre en 1 et 100, vies {vies}: ")

    response = int(response)
    vies -= 1

    if response != chiffre_a_deviner and vies > 0:

        if response <= chiffre_a_deviner:
            print("Bien essayé trop petit")
        else:
            print("Bien essayé trop grand")

# fin de jeu
if response == chiffre_a_deviner:
    print(f"Bravo tu as trouvé le chiffre exact en {7 - vies} essais")
else:
    print(f"Dommage le chiffre était {chiffre_a_deviner}")
