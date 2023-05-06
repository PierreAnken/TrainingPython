liste=[]
for chiffre in range(700,1100):
    if chiffre % 7==0 and chiffre %5!=0 and chiffre %2!=0:
        liste.append(chiffre)
print(liste)


