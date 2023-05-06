def inverse(some_pile):
    # on vide la pile
    ma_liste = []
    while some_pile:
        ma_liste.append(some_pile.pop())

    # on la re-remplit dans l'ordre inverse
    for valeur in ma_liste:
        some_pile.append(valeur)


def invert(some_pile, buffer):
    if some_pile:
        buffer.append(some_pile.pop())
        invert(some_pile, buffer)
        some_pile.append(buffer.pop(0))



pile = [5, "bonjour", 8.35, True]
invert(pile, [])
print(pile)
