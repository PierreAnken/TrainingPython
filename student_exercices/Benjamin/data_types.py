liste1 = []
liste1.append("apple")
liste1.insert(0, "Birne")

liste1[0], liste1[1] = liste1[1], liste1[0]
liste1 = liste1 * 5
liste1 = liste1[-2:]
liste1.extend(("Orange", "Zitrone"))

print(liste1)

