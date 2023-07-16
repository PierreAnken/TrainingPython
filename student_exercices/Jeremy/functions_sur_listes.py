# EX 1

# my_list = ['mange', 'passe', 'dansent', 'tortue', 'belette',
#            'caravane', 'la', 'la', 'les', 'renard', 'tortue', 'aboient',
#            'dort', 'le', 'tortue', 'chiens', 'chat', 'loup', 'les', 'le',
#            'le', 'cheval']
#
# print(len(my_list))
#
# print(my_list.count('tortue'))
#
# del my_list[0]
# print(my_list)
#
# del my_list[-1]
# print(my_list)
#
# while 'tortue' in my_list:
#     my_list.remove('tortue')
# print(my_list)
#
# my_list.insert(4,'souris')
#
# my_list.reverse()
# print(my_list[::3])
# print(my_list[1::3])
# print(my_list[2::3])

# EX 2

# l1 = [0, 1, 2]
# l2 = l1
# l3 = l1.copy()
# l2.append(20)
# l3.append(30)
# print("l1=", l1, id(l1))
# print("l2=", l2, id(l2))
# print("l3=", l3, id(l3))

# EX 3

# phrase="Le soleil brille, les oiseaux chantent"
# liste=phrase.split(" ")
# print(liste)

# EX 4
# l=['Maître', 'Renard', 'sur', 'son', 'arbre', 'perché...']
# phrase=" ".join(l)
# print(phrase)

# EX 5

# Mémoriser et récupérer des données dans un fichier
# instructions open, write, read
# fichier = open("mon_fichier.txt", "a")
# fichier.write("Bonjour tout le monde ! ")
# fichier.close()
#
# fichier = open("mon_fichier.txt", "r")
# print(fichier.read())
# fichier.close()

# EX 6
# def saisir_txt(nom_fichier):
#     fichier = open(nom_fichier, "a")
#     fichier.write(input('Phrase: ')+ "\n")
#     fichier.close()
#
# # saisir_txt('file.txt')
# # saisir_txt('file.txt')
#
# def lire_txt(nom_fichier):
#     fichier = open(nom_fichier,"r")
#     return fichier.read().split('\n')
#
# print(lire_txt('file.txt'))

