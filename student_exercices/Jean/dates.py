
# On définit une variable avec une valeur "vide"
age_int = None

# Tant que l'utilisateur n'a pas donné de réponse valide
while not age_int:
    # On récupère la réponse de l'utilisateur. Attention: ne pas écraser la variable vide directement.
    age_str = input("Quel est votre age ?")
    # Si l'entrée de l'utilisateur est valide
    if age_str.isdigit() and 5 <= int(age_str) <= 120:
        # On la sauvegarde après conversion
        age_int = int(age_str)

annee = None
while not annee:
    annee_str = input("Quelle année sommes-nous ?")
    if annee_str.isdigit():
        annee = int(annee_str)

jours_vecus = int(age_int * 365.25)


print(f"""
Vous  avez {age_int} ans.
L'an prochain vous aurez {age_int + 1} ans.
Dans 15 ans, vous aurez {age_int + 15} ans.
Vous avez vécu {jours_vecus} jours depuis votre naissance.
""")


