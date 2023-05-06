def counter_letter(lettre_a_compter, texte):
    """
    :param lettre_a_compter: une lettre
    :param texte: un texte
    :return: le nombre de foix que la lettre apparaît dans le texte
    """

    nombre_occurence = 0
    for lettre in texte:
        if lettre == lettre_a_compter:
            nombre_occurence += 1

    return nombre_occurence


# print(counter_letter("a", "abcdefabc"))


def cache_lettre(texte):
    """
    :param texte:un texte
    :return: un nouveau texte, où les lettres sont remplacées par des "_"
    """

    text_cache = ''
    for caractere in texte:
        if caractere.isalpha():  # isalpha() => return True si c'est une lettre de l'alphabet
            text_cache += '_'
        else:
            text_cache += caractere
    return text_cache


texte_test = 'A la claire fontaine...'
print(cache_lettre(texte_test))
