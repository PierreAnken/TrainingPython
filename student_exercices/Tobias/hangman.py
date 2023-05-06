import random

import requests

from string import ascii_lowercase as alphabet


def get_quote_from_api(url: str) -> str:  # after -> refers to the return value
    """
    Given an url we are getting back a quote from the website
    :param url: endpoint url from quotes api
    :return: randomly chosen quote
    """
    response = requests.get(url)
    quote_list = response.json()  # [{},{}]
    index_quote = random.randint(0, len(quote_list) - 1)  # [0 ... x]
    quote_dict = quote_list[index_quote]  # quote_list[y] => {'author':'xxx', 'text':'xxx'}
    return quote_dict['text']  # str


def get_hidden_sentence(sentence: str) -> str:
    """
    Given a sentence we are getting back the sentence with any letters replaced by blank spaces
    :param sentence: any sentence
    :return: sentence in hidden format
    """
    hidden_sentence = ''

    # convert the given sentence
    for character in sentence:
        if character.lower() in alphabet:
            hidden_sentence += '_'
        else:
            hidden_sentence += character

    return hidden_sentence


def guess_letter(some_quote: str) -> (bool, str):
    """

    :param some_quote: any letter in the alphabet
    :return:
    """
    some_letter = ''

    while some_letter.lower() not in alphabet or len(some_letter) != 1:
        some_letter = input("Please enter a letter: ")

    return some_letter in some_quote, some_letter.lower()


# Methode zeigt Buchstabe in hidden_quote
def reveal_letter(some_letter, some_quote, some_hidden_quote):
    """
    Given the values of a letter a quote and a hidden quote - this method reveals the letters in the hidden quote
    :param some_letter: any letter
    :param some_quote: any quote
    :param some_hidden_quote: any hidden quote
    :return: the changed sentence
    """
    sentence = ''

    for base_letter, hidden_letter in zip(some_quote, some_hidden_quote):
        if some_letter == base_letter.lower():
            sentence += base_letter
        else:
            sentence += hidden_letter

    return sentence


# Wird ein Satz definiert
# Werden die leeren Buchstabenfelder der Wörter aufgeschrieben
# Dann gibt es einen Hangman, der x Wiederholungen zulässt und dann das Spiel beendet, wenn zu oft falsch geraten wurde

# Die Spieler raten Buchstaben
# Reaktion: Richtig geraten: Buchstabe kommt rein
# Rekation: Falsch geraten: Der Hangman counter wird +1 gezähglt - es wird ein Symbol am Hangman hinzugefügt

# Gewonnen, wenn der Satz voll dasteht bevor der Hangman fertig ist
# Verloren wenn der Hangman fertig ist bevor der Satz steht

if __name__ == '__main__':

    api_url = 'https://type.fit/api/quotes'
    quote = get_quote_from_api(api_url)
    # following line comments sentence: print(quote)

    hidden_quote = get_hidden_sentence(quote)
    lives = 5

    while lives > 0 and '_' in hidden_quote:
        print(hidden_quote)
        is_in_quote, letter = guess_letter(quote)

        if is_in_quote:
            hidden_quote = reveal_letter(letter, quote, hidden_quote)
        else:
            lives -= 1
            if lives > 0:
                print(f'{letter} is not contained in the sentence. Your new live count is {lives}.')
            else:
                print(f'Game Over. The quote was: "{quote}"')

    print(guess_letter(quote))

