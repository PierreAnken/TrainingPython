"""
EXERCICE : GESTION D'UN CHAMPIONNAT DE FOOTBALL (POO)
Difficulté : Intermédiaire - 10 étapes progressives

OBJECTIF : Implémenter les classes Personne, Joueur, Arbitre, Entraineur, Equipe, Match, Stade et Championnat.
L'exercice se fait en complétant les fichiers correspondants.

CONSIGNES :
1.  Classe Personne : Ajouter un constructeur avec 'nom' (str) et 'age' (int).
2.  Classe Personne : Ajouter la méthode __str__ pour afficher "[nom] ([age] ans)".
3.  Classe Joueur : Hériter de Personne. Ajouter le constructeur avec 'poste' et 'numero'.
    - Appeler le constructeur parent.
    - Surcharger __str__ pour afficher "Joueur [numero]: [nom] ([age] ans) - [poste]".
4.  Classe Arbitre : Hériter de Personne. Ajouter le constructeur avec 'experience' (int).
    - Appeler le constructeur parent.
    - Surcharger __str__ pour afficher "Arbitre [nom] ([age] ans) ([experience] ans d'XP)".
5.  Classe Equipe : Ajouter la méthode 'ajouter_joueur(joueur)' :
    - Vérifier que 'joueur' est bien une instance de Joueur.
    - Ajouter le joueur seulement si l'équipe contient moins de 11 joueurs.
6.  Classe Match : Ajouter la méthode 'marquer_but(est_domicile)' pour incrémenter le score.
7.  Classe Match : Ajouter une méthode statique 'duree_reglementaire()' qui retourne 90.
8.  Classe Stade : Ajouter la méthode __str__ : "[nom] à [ville] ([capacite] places)".
9.  Classe Championnat : Ajouter la méthode 'inscrire_equipe(equipe)'.
10. S'assurer de la cohérence globale des affichages.

LANCEZ LE FICHIER POUR VÉRIFIER VOS RÉPONSES.
"""

from personne import Personne
from joueur import Joueur
from arbitre import Arbitre
from entraineur import Entraineur
from equipe import Equipe
from match import Match
from stade import Stade
from championnat import Championnat

def tester_exercice():
    points = 0
    print("=== VÉRIFICATION DE L'EXERCICE FOOTBALL ===\n")

    # 1. Test Personne __init__
    try:
        p_test = Personne("Test", 20)
        if hasattr(p_test, 'nom') and p_test.nom == "Test":
            print("Point 1 (Init Personne) : OK")
            points += 1
        else:
            print("Point 1 (Init Personne) : ERREUR (Attributs non initialisés)")
    except Exception as e:
        print(f"Point 1 (Init Personne) : ERREUR ({e})")

    # 2. Test Héritage Personne -> Joueur/Arbitre/Entraineur
    try:
        j1 = Joueur("Mbappé", 25, "Attaquant", 10)
        a1 = Arbitre("Turpin", 42, 15)
        e1 = Entraineur("Deschamps", 55, "Pro")
        
        if isinstance(j1, Personne) and isinstance(a1, Personne) and isinstance(e1, Personne):
            print("Point 2 (Héritage) : OK")
            points += 1
        else:
            print("Point 2 (Héritage) : ERREUR (Les classes doivent hériter de Personne)")
    except Exception as e:
        print(f"Point 2 (Héritage) : ERREUR ({e})")

    # 3. Test Personne __str__
    try:
        p1 = Personne("Dupont", 30)
        if str(p1) == "Dupont (30 ans)":
            print("Point 3 (Str Personne) : OK")
            points += 1
        else:
            print(f"Point 3 (Str Personne) : ERREUR (Reçu: {str(p1)})")
    except Exception as e:
        print(f"Point 3 (Str Personne) : ERREUR ({e})")

    # 4. Test Joueur __str__
    try:
        if str(j1) == "Joueur 10: Mbappé (25 ans) - Attaquant":
            print("Point 4 (Str Joueur) : OK")
            points += 1
        else:
            print(f"Point 4 (Str Joueur) : ERREUR (Reçu: {str(j1)})")
    except Exception as e:
        print(f"Point 4 (Str Joueur) : ERREUR ({e})")

    # 5. Test Arbitre __str__
    try:
        if str(a1) == "Arbitre Turpin (42 ans) (15 ans d'XP)":
            print("Point 5 (Str Arbitre) : OK")
            points += 1
        else:
            print(f"Point 5 (Str Arbitre) : ERREUR (Reçu: {str(a1)})")
    except Exception as e:
        print(f"Point 5 (Str Arbitre) : ERREUR ({e})")

    # 6. Test Equipe ajouter_joueur (limite 11)
    try:
        equipe = Equipe("France", e1)
        for i in range(12):
            equipe.ajouter_joueur(Joueur(f"J{i}", 20, "Poste", i))
        
        if len(equipe.joueurs) == 11:
            print("Point 6 (Ajout Joueur/Limite) : OK")
            points += 1
        else:
            print(f"Point 6 (Ajout Joueur/Limite) : ERREUR (Taille attendue 11, reçue {len(equipe.joueurs)})")
    except Exception as e:
        print(f"Point 6 (Ajout Joueur/Limite) : ERREUR ({e})")

    # 7. Test Match marquer_but
    try:
        equipe2 = Equipe("Espagne", Entraineur("De la Fuente", 60, "Pro"))
        match = Match(equipe, equipe2, a1)
        match.marquer_but(True)  # But domicile
        match.marquer_but(False) # But extérieur
        match.marquer_but(True)  # But domicile
        
        if match.score == (2, 1):
            print("Point 7 (Score Match) : OK")
            points += 1
        else:
            print(f"Point 7 (Score Match) : ERREUR (Score attendu (2, 1), reçu {match.score})")
    except Exception as e:
        print(f"Point 7 (Score Match) : ERREUR ({e})")

    # 8. Test Match fonction statique
    try:
        if Match.duree_reglementaire() == 90:
            print("Point 8 (Fonction Statique) : OK")
            points += 1
        else:
            print("Point 8 (Fonction Statique) : ERREUR")
    except Exception as e:
        print(f"Point 8 (Fonction Statique) : ERREUR ({e})")

    # 9. Test Stade __str__
    try:
        stade = Stade("Stade de France", "Saint-Denis", 80000)
        if str(stade) == "Stade de France à Saint-Denis (80000 places)":
            print("Point 9 (Str Stade) : OK")
            points += 1
        else:
            print(f"Point 9 (Str Stade) : ERREUR (Reçu: {str(stade)})")
    except Exception as e:
        print(f"Point 9 (Str Stade) : ERREUR ({e})")

    # 10. Test Championnat inscrire_equipe
    try:
        ligue1 = Championnat("Ligue 1", "France")
        ligue1.inscrire_equipe(equipe)
        if len(ligue1.equipes) == 1 and str(ligue1) == "Ligue 1 (France) - 1 équipes engagées":
            print("Point 10 (Championnat & Cohérence) : OK")
            points += 1
        else:
            print("Point 10 (Championnat & Cohérence) : ERREUR")
    except Exception as e:
        print(f"Point 10 (Championnat & Cohérence) : ERREUR ({e})")

    print(f"\nSCORE FINAL : {points}/10")
    if points == 10:
        print("FÉLICITATIONS ! Tu es le champion du monde.")

if __name__ == "__main__":
    tester_exercice()
