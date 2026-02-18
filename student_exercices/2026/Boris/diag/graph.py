import pandas as pd
import matplotlib.pyplot as plt

# 1. Daten aus der Excel-Datei laden
# Wir verwenden den Dateinamen im selben Ordner
dateipfad = 'AHV Tabelle 2026.xlsx'
df = pd.read_excel(dateipfad)

# 2. Spalten identifizieren
# Spalte A: Jahres-Einkommen -> X-Achse
# Spalte B: Alters-/Invalidenrente annualisiert -> Verwendet für die Y-Achse
# Hinweis: Die Spaltennamen müssen exakt wie in der Excel-Datei sein.
spalte_x = 'Jahres‑Einkommen'
spalte_y_wert = 'Alters‑/Invalidenrente annualisiert'

# 3. Y-Achse berechnen: Spalte B als Prozentsatz von Spalte A
# Formel: (Rente / Einkommen) * 100
df['Rente_in_Prozent'] = (df[spalte_y_wert] / df[spalte_x]) * 100

# 4. Grafik erstellen
plt.figure(figsize=(10, 6)) # Bildgröße festlegen
plt.plot(df[spalte_x], df['Rente_in_Prozent'], marker='o', linestyle='-', color='blue')

# 5. Titel und Beschriftungen hinzufügen (für bessere Lesbarkeit)
plt.title('Rente in % des Jahreseinkommens (AHV 2026)', fontsize=14)
plt.xlabel('Jahres-Einkommen (A)', fontsize=12)
plt.ylabel('Rente in % des Einkommens (B % von A)', fontsize=12)

# Raster hinzufügen, um das Lesen der Punkte zu erleichtern
plt.grid(True)

# 6. Grafik anzeigen oder speichern
# Da dies ein Skript ist, speichern wir es als Bild
plt.savefig('graphique_ahv.png')
print("Die Grafik wurde erfolgreich in der Datei 'graphique_ahv.png' erstellt.")

# Wenn du es auf deinem Computer ausführst, kannst du die folgende Zeile einkommentieren:
# plt.show()
