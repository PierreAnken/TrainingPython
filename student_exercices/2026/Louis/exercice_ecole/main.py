"""
EXERCICE : GESTION D'UNE ÉCOLE (POO)
Difficulté : Débutant - 10 étapes progressives

OBJECTIF : Implémenter les classes Eleve, SalleDeClasse et Ecole avec leurs méthodes.
L'exercice se fait en complétant les fichiers correspondants (eleves.py, salle_de_classe.py, ecole.py).

CONSIGNES :
1.  Classe Eleve : Ajouter un constructeur avec 'nom' et 'note'.
2.  Classe Eleve : Ajouter la méthode __str__ pour afficher "Élève : [nom] (Note: [note])".
3.  Classe Eleve : Ajouter la méthode __eq__ pour comparer deux élèves sur leur note (==).
4.  Classe SalleDeClasse : Ajouter un constructeur avec 'nom_classe' et une liste d'élèves vide 'eleves' par défaut.
5.  Classe SalleDeClasse : Ajouter la méthode 'ajouter_eleve(eleve)'.
6.  Classe SalleDeClasse : Ajouter la méthode __len__ pour obtenir le nombre d'élèves.
7.  Classe SalleDeClasse : Ajouter la méthode 'moyenne_classe()' qui retourne la moyenne des notes.
8.  Classe Ecole : Ajouter un constructeur avec 'nom_ecole' et une liste de salles 'salles' vide par défaut.
9.  Classe Ecole : Ajouter la méthode 'ajouter_salle(salle)'.
10. Classe Ecole : Ajouter la méthode __str__ qui affiche le nom de l'école et le total d'élèves cumulé.

LANCEZ LE FICHIER POUR VÉRIFIER VOS RÉPONSES.
"""

# --- VOTRE CODE ICI ---

from eleves import Eleve
from salle_de_classe import SalleDeClasse
from ecole import Ecole


# --- TESTS DE VALIDATION (NE PAS MODIFIER) ---

def tester_exercice():
    points = 0
    print("=== VÉRIFICATION DE L'EXERCICE ===\n")

    # 1. Test Eleve __init__
    try:
        e1 = Eleve("Alice", 15)
        e2 = Eleve("Bob", 12)
        if e1.nom == "Alice" and e1.note == 15:
            print("Point 1 (Init Eleve) : OK")
            points += 1
        else:
            print("Point 1 (Init Eleve) : ERREUR (Attributs mal nommés)")
    except Exception as e:
        print(f"Point 1 (Init Eleve) : ERREUR ({e})")

    # 2. Test Eleve __str__
    try:
        if str(e1) == "Élève : Alice (Note: 15)":
            print("Point 2 (Str Eleve) : OK")
            points += 1
        else:
            print(f"Point 2 (Str Eleve) : ERREUR (Attendu 'Élève : Alice (Note: 15)', reçu '{str(e1)}')")
    except Exception as e:
        print(f"Point 2 (Str Eleve) : ERREUR ({e})")

    # 3. Test Eleve __eq__
    try:
        e3 = Eleve("Charlie", 15)
        if e1 == e3 and not (e1 == e2):
            print("Point 3 (Eq Eleve) : OK")
            points += 1
        else:
            print("Point 3 (Eq Eleve) : ERREUR (La comparaison doit se baser sur la note)")
    except Exception as e:
        print(f"Point 3 (Eq Eleve) : ERREUR ({e})")

    # 4. Test SalleDeClasse __init__
    try:
        s1 = SalleDeClasse("Informatique")
        if s1.nom_classe == "Informatique" and isinstance(s1.eleves, list):
            print("Point 4 (Init Salle) : OK")
            points += 1
        else:
            print("Point 4 (Init Salle) : ERREUR (Attributs mal nommés ou liste manquante)")
    except Exception as e:
        print(f"Point 4 (Init Salle) : ERREUR ({e})")

    # 5. Test ajouter_eleve
    try:
        s1.ajouter_eleve(e1)
        s1.ajouter_eleve(e2)
        if e1 in s1.eleves and len(s1.eleves) == 2:
            print("Point 5 (Ajout Eleve) : OK")
            points += 1
        else:
            print("Point 5 (Ajout Eleve) : ERREUR (L'élève n'a pas été ajouté)")
    except Exception as e:
        print(f"Point 5 (Ajout Eleve) : ERREUR ({e})")

    # 6. Test SalleDeClasse __len__
    try:
        if len(s1) == 2:
            print("Point 6 (Len Salle) : OK")
            points += 1
        else:
            print("Point 6 (Len Salle) : ERREUR (Doit retourner le nombre d'élèves)")
    except Exception as e:
        print(f"Point 6 (Len Salle) : ERREUR ({e})")

    # 7. Test moyenne_classe
    try:
        moyenne = s1.moyenne_classe()
        if moyenne == 13.5:
            print("Point 7 (Moyenne Classe) : OK")
            points += 1
        else:
            print(f"Point 7 (Moyenne Classe) : ERREUR (Attendu 13.5, reçu {moyenne})")
    except Exception as e:
        print(f"Point 7 (Moyenne Classe) : ERREUR ({e})")

    # 8. Test Ecole __init__
    try:
        ecole = Ecole("Lycée Python")
        if ecole.nom_ecole == "Lycée Python" and isinstance(ecole.salles, list):
            print("Point 8 (Init Ecole) : OK")
            points += 1
        else:
            print("Point 8 (Init Ecole) : ERREUR (Attributs mal nommés ou liste manquante)")
    except Exception as e:
        print(f"Point 8 (Init Ecole) : ERREUR ({e})")

    # 9. Test ajouter_salle
    try:
        ecole.ajouter_salle(s1)
        if s1 in ecole.salles:
            print("Point 9 (Ajout Salle) : OK")
            points += 1
        else:
            print("Point 9 (Ajout Salle) : ERREUR (La salle n'a pas été ajoutée)")
    except Exception as e:
        print(f"Point 9 (Ajout Salle) : ERREUR ({e})")

    # 10. Test Ecole __str__
    try:
        # On ajoute une 2eme salle avec 1 eleve pour tester le total
        s2 = SalleDeClasse("Maths")
        s2.ajouter_eleve(Eleve("David", 10))
        ecole.ajouter_salle(s2)
        description = str(ecole)
        if "Lycée Python" in description and "3" in description:
            print("Point 10 (Str Ecole) : OK")
            points += 1
        else:
            print(f"Point 10 (Str Ecole) : ERREUR (Doit contenir le nom et le total d'élèves : '{description}')")
    except Exception as e:
        print(f"Point 10 (Str Ecole) : ERREUR ({e})")

    print(f"\nSCORE FINAL : {points}/10")
    if points == 10:
        print("FÉLICITATIONS ! Tout est correct.")


if __name__ == "__main__":
    tester_exercice()
