# def inverse(nombre):
#     return -nombre
#
#
#
# if inverse(-5) != 5:
#     print(f'Erreur, attendu {5} retourné {inverse(-5)}')

# def inverse(liste):
#     return liste[::-1]
#
# if inverse([1,'a',3.3]) != [3.3,'a',1]:
#     print(f"Erreur, attendu {[3.3,'a',1]} retourné {inverse([1,'a',3.3])}")
# def multi3(n):
#     return list(range(3, n, 3))
#
#
# if multi3(20) != [3, 6, 9, 12, 15, 18]:
#     print(f"Erreur, attendu {[3, 6, 9, 12, 15, 18]} retourné {multi3(20)}")
#
# def lettres_communes(n, m):
#     mot_sortie = ""
#     for lettre in n:
#         if lettre not in mot_sortie:
#             if lettre in m:
#                 mot_sortie += lettre
#     return mot_sortie

# def lettres_communes(n, m):
#     intersection = set(list(n)).intersection(set(list(m)))
#     return ''.join(intersection)
#
# if lettres_communes('abcdefffabc', 'cdeeeeeezuuu') != 'cde':
#     print(f"Erreur, attendu cde retourné {lettres_communes('abcdefffabc', 'cdeeeeeezuuu')}")
# from random import randint
#
#
# def moyenne(n):
#     somme = 0
#     for _ in range(n):
#         somme += randint(0, 100)
#     return somme / n
#
#
# for x in [10, 100, 1000, 100000]:
#     print(moyenne(x))
#
# def palindrome(mot):
#     return mot == mot[::-1]
#
#
# print(palindrome("kayak"))

# def bisextille(annee):
#     return annee % 4 == 0
# print(bisextille(2021))

from string import ascii_lowercase as alphabet
def somme(mot):
    somme = 0
    for x in mot:
        somme += alphabet.index(x)
    return somme
print(somme("abc"))
