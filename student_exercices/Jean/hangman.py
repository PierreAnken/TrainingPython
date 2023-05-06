import random

import requests


def get_quotes(url):
    # Make a GET request and get response data
    response = requests.get(url)

    # parse json and get the quote list back
    data = response.json()
    return data


def get_citation_cachee(some_citation: str):
    some_citation_cachee = ''
    for signe in some_citation:
        if signe.isalpha():
            some_citation_cachee += '_'
        else:
            some_citation_cachee += signe
    return some_citation_cachee


def affiche_lettre(some_citation, some_citation_cachee, some_guess):
    citation_cachee_revelee = ''

    # zip: boucles en parallèles
    for lettre_citation, lettre_cachee in zip(some_citation, some_citation_cachee):

        if lettre_citation == some_guess or lettre_cachee != '_':
            citation_cachee_revelee += lettre_citation
        else:
            citation_cachee_revelee += lettre_cachee

    return citation_cachee_revelee


if __name__ == '__main__':
    # Get all quotes from api
    api_url = 'https://type.fit/api/quotes'
    all_quotes = get_quotes(api_url)

    # Jeu du pendu résumé:
    # tu dois deviner un mot en proposant des lettres les unes après les autres.
    # Tu as droit à X vie. Si tu te trompes on enlève une vie et pour finir tu seras pendu.

    # Jeu du pendu étapes:

    # Une phrase que tu ne connais pas est choisie
    citation_dict = random.sample(all_quotes, 1)[0]
    citation, auteur = citation_dict['text'], citation_dict['author']
    # print(citation, auteur)

    citation_cachee = get_citation_cachee(citation)

    vies = 7

    # Tant que tu n'as pas découvert la phrase et que tu as encore des vies (tu débutes à 7)
    while vies > 0 and '_' in citation_cachee:

        print(citation_cachee)

        # Tu proposes une lettre
        guess = input(f"Propose une lettre ({vies} vies): ")

        # Si la lettre est dans le mot => on la dévoile dans la phrase cachée
        if guess in citation:
            citation_cachee = affiche_lettre(citation, citation_cachee, guess)

        # Si la lettre n'est pas dans le mot on t'enlève une vie.
        else:
            vies -= 1

    # A la fin tu as soit gagné soit perdu
    if vies > 0:
        print('Bravo tu as gagné')
    else:
        print('Dommage, tu as perdu.')