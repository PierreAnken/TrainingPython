list_1 = {"prenom": "Pierre", "nom": "Blanc", "age": "34", "adresse": "chemin des Bleus 4", "npa": "1211",
          "ville": "Genève"}, \
         {"prenom": "Louise", "nom": "Blanc", "age": "37", "adresse": "chemin des Voeux 18",
          "npa": "1222", "ville": "Icyela"}, \
         {"prenom": "André", "nom": "Carré", "age": "28",
          "adresse": "chemin des Vieux 18", "npa": "1244",
          "ville": "Bernex"}, \
         {"prenom": "Loan",
          "nom": "Gerber", "age": "22",
          "adresse": "rue du Lac 11",
          "npa": "3963",
          "ville": "Crans-vers-la-Montagne"}, \
         {
             "prenom": "Louise", "nom": "Blanc", "age": "37", "adresse": "chemin des Voeux 18", "npa": "1222",
             "ville": "Icyela"}

# Me montrer comment:
# quelles différences entre les , ou les : dans une liste ?
# mettre à la ligne avec \n
# peut-on extraire tous les prénoms, adresses... ?
#

liste_prenoms, liste_noms = [], []
for personne in list_1:
    liste_prenoms.append(personne['prenom'])
    liste_noms.append(personne['nom'])
print(liste_prenoms, liste_noms)
