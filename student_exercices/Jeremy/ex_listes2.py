
liste_vide = []
liste_vide.extend(['abc',23])
liste_vide.insert(0,'hello')
liste_vide.append('voyage')
liste_vide.insert(int(len(liste_vide)/2),4)
liste_vide[4]+='s'
liste_vide[2]**=2
liste_vide.append(liste_vide.pop(1))
liste_vide[2] = int(str(liste_vide[2])[1]+str(liste_vide[2])[0])



print(liste_vide)


