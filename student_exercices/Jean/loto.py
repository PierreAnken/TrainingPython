import random

chiffres = list(range(1, 51))
etoiles = list(map(lambda c: c * '*', range(1, 8)))

# 5 chiffres et 2 etoiles
tirage = []
for _ in range(5):
    index_chiffre = random.randint(0, len(chiffres)-1)
    tirage.append(chiffres.pop(index_chiffre))

tirage_etoile = []
for _ in range(2):
    index_etoiles = random.randint(0, len(etoiles)-1)
    tirage_etoile.append(etoiles.pop(index_etoiles))

tirage.sort()
tirage_etoile.sort()

print(tirage+tirage_etoile)
