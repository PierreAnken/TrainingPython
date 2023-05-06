# Ecrivez un programme qui affiche un triangle isocèle de hauteur h ( nombre à rentrer par l'utilisateur) avec des X.

  #
 ###
#####

# ligne 0 => 2 espaces / 1 caractère
# ligne 1 => 1 espaces / 3 caractère
# ligne 2 => 0 espaces / 5 caractère


n = int(input('Entrez n: '))

base_triangle = (n*2)-1
for num_ligne in range(n):
    largueur_ligne = ((num_ligne+1) * 2) - 1
    espaces_gauche = (base_triangle-largueur_ligne)//2
    print(espaces_gauche*' '+largueur_ligne*'X')
