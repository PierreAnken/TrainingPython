"""
Wiederholungsübung 3: Grundlagen von Python (Teile 0 bis 5)
Identifizieren Sie das Ergebnis für jeden Punkt oder beantworten Sie die gestellte Frage.
"""

# 1. Was ist das Ergebnis dieser Berechnung?
# 2 ** 3 + 4
antwort1 = 12

# 2. Was ist der Endwert von 'liste' nach dieser Operation?
liste = [10, 20, 30]
liste.pop(1)
# antwort2 = 
antwort2 = [10, 30]

# 3. Welchen Wert hat 's2'?
s1 = "Hallo"
s2 = s1.lower()
# antwort3 = 
antwort3 = "hallo"

# 4. Was ist das Ergebnis dieses Vergleichs?
# 10 == "10"
antwort4 = False

# 5. Was ist die Länge dieses Sets?
mein_set = {1, 2, 2, 3, 3, 3}
# len(mein_set)
antwort5 = 3

# 6. Welchen Wert hat 'ergebnis'?
a = 5
b = 10
ergebnis = (a > 2) and (b < 15)
antwort6 = True

# 7. Was passiert in diesem Dictionary?
preise = {"Apfel": 1.5, "Birne": 2.0}
preise["Apfel"] = 1.8
# Welchen Wert hat preise["Apfel"] jetzt?
antwort7 = 1.8

# 8. Welcher Typ ist das Ergebnis von: 10 / 2
# (Geben Sie den Typ-Namen ein, z.B. int, str, float, bool)
# Hinweis: Benutzen Sie type(10 / 2)
antwort8 = float

# 9. Was wird dieser bedingte Block anzeigen?
alter = 15
if alter >= 18:
    status = "Erwachsen"
elif alter >= 12:
    status = "Jugendlich"
else:
    status = "Kind"
antwort9 = "Jugendlich"

# 10. Wie fügt man das Element '4' an den Anfang der Liste [1, 2, 3] ein?
# Geben Sie den Namen der Methode an (z.B. "append", "extend", "insert")
# Syntax: liste.methodenname(0, 4)
antwort10 = 'insert'

# --- TESTS ---
print("\n=== ÜBUNGSERGEBNISSE 3 ===")

# Korrekte Antworten berechnen
korrekt1 = 2 ** 3 + 4
korrekt2 = [10, 30]
korrekt3 = "hallo"
korrekt4 = 10 == "10"
korrekt5 = len({1, 2, 2, 3, 3, 3})
korrekt6 = (5 > 2) and (10 < 15)
korrekt7 = 1.8
korrekt8 = type(10 / 2)
korrekt9 = "Jugendlich"
korrekt10 = "insert"

results = [
    (1, antwort1, korrekt1),
    (2, antwort2, korrekt2),
    (3, antwort3, korrekt3),
    (4, antwort4, korrekt4),
    (5, antwort5, korrekt5),
    (6, antwort6, korrekt6),
    (7, antwort7, korrekt7),
    (8, antwort8, korrekt8),
    (9, antwort9, korrekt9),
    (10, antwort10, korrekt10)
]

punkte = 0
for nr, user, real in results:
    if user == real:
        print(f"Frage {nr}: Richtig! ✅")
        punkte += 1
    else:
        print(f"Frage {nr}: Falsch ❌")

print(f"\nGesamtpunktzahl: {punkte}/10")
