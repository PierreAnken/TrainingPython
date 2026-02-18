"""
Wiederholungsübung 4: Schleifen (Teile 0 bis 7)
Identifizieren Sie das Ergebnis für jeden Punkt oder beantworten Sie die gestellte Frage.
Vervollständigen Sie die Variablen 'antwort1' bis 'antwort10'.
"""

# 1. Wie oft wird "Hallo" gedruckt?
# for i in range(5):
#     print("Hallo")
antwort1 = None

# 2. Welchen Wert hat 'summe' am Ende?
summe = 0
for zahl in [1, 2, 3, 4]:
    summe += zahl
# antwort2 = 
antwort2 = None

# 3. Was ist der letzte Wert von 'i', der gedruckt wird?
# i = 0
# while i < 10:
#     i += 3
#     print(i)
antwort3 = None

# 4. Welchen Wert hat 'index' beim Buchstaben 'c'?
# alphabet = "abcde"
# for index, buchstabe in enumerate(alphabet):
#     if buchstabe == 'c':
#         break
antwort4 = None

# 5. Was wird in dieser Schleife übersprungen (continue)?
# ergebnis = []
# for x in range(5):
#     if x % 2 == 0:
#         continue
#     ergebnis.append(x)
# Welchen Wert hat 'ergebnis' am Ende?
antwort5 = None

# 6. Was ist das Ergebnis dieser verschachtelten Schleife?
# count = 0
# for i in range(2):
#     for j in range(3):
#         count += 1
antwort6 = None

# 7. Welchen Wert hat 'paare' am Ende?
# liste1 = [1, 2]
# liste2 = ['a', 'b']
# paare = list(zip(liste1, liste2))
antwort7 = None

# 8. Was passiert, wenn die Schleife NICHT durch 'break' unterbrochen wird?
# text = ""
# for n in range(3):
#     if n > 5:
#         break
# else:
#     text = "Fertig"
# Welchen Wert hat 'text' am Ende?
antwort8 = None

# 9. Wie viele Elemente hat range(2, 10, 2)?
# (Geben Sie die Anzahl als Ganzzahl an)
antwort9 = None

# 10. Was ist der Wert von 's' am Ende?
# s = ""
# for char in "Python":
#     if char == "h":
#         break
#     s += char
antwort10 = None


# --- TESTS ---
# Diese Sektion nicht ändern! Sie dient zur Überprüfung Ihrer Antworten.
if __name__ == "__main__":
    print("\n=== ÜBUNGSERGEBNISSE 4 (Schleifen) ===")

    korrekt1 = 5
    korrekt2 = 10
    korrekt3 = 12
    korrekt4 = 2
    korrekt5 = [1, 3]
    korrekt6 = 6
    korrekt7 = [(1, 'a'), (2, 'b')]
    korrekt8 = "Fertig"
    korrekt9 = 4
    korrekt10 = "Pyt"

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
            if user is None:
                print(f"Frage {nr}: Noch nicht beantwortet ⏳")
            else:
                print(f"Frage {nr}: Falsch ❌")

    print(f"\nGesamtpunktzahl: {punkte}/10")
