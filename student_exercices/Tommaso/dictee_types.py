liste = [
    0,
    ("m", 5, 4.6),
    {
        25: "abc",
        "bonjour": 236,
        "date": [28, 2, 2023],
    }
]
print(liste[2]["bonjour"])
print(liste[2]["date"][1])

liste[2]["date"].append(19)
print(liste[2]["date"])

del liste[2][25]
print(liste[2])

liste[2]["bonjour"] = "Tommaso"
print(liste[2])

del liste[1]
print(liste)

liste[1]["date"][0], liste[1]["date"][2] = liste[1]["date"][2], liste[1]["date"][0]
print(liste)



