import random

import requests


def get_quotes(url, anzahl=5):
    # Make a GET request and get response data
    response = requests.get(url)

    # parse json and get the quote list back
    data = response.json()

    quotes = [dictionary['text'] for dictionary in data]
    return quotes[:anzahl]


def get_hidden_quote(some_quote):
    # 'We can only' => '__ ___ ____'

    # create empty string (hidden_quote)
    hidden_quote = ''
    # for each letter in quote
    for letter in some_quote:
        # if a letter => add '_' to string
        if letter.isalpha():
            hidden_quote += '_'

        # else add the symbol
        else:
            hidden_quote += letter
    # return the hidden quote
    return hidden_quote


def reveal_letter_in_quote(some_letter: str, some_quote: str, some_hidden_quote: str) -> str:
    # some_quote = 'We can only'
    # some_hidden_quote = '__ ___ ____'
    # some_letter = 'a'

    new_hidden_quote = ''
    # for each letter from the quote
    for letter, letter_hidden in zip(some_quote, some_hidden_quote):

        # if the letter is not _ => copy it to new_hidden_quote
        if letter_hidden != '_' or letter.lower() == some_letter.lower():
            new_hidden_quote += letter
        else:
            # else add _
            new_hidden_quote += '_'

    return new_hidden_quote


if __name__ == '__main__':
    api_url = 'https://type.fit/api/quotes'

    quote_list = get_quotes(api_url, 20)

    # Ein Satz wälen
    quote = random.sample(quote_list, 1)[0]
    quote_hidden = get_hidden_quote(quote)
    # print(quote, '\n', quote_hidden, sep='')

    # Anzahl Leben
    leben = 10

    while leben != 0 and quote != quote_hidden:

        print(quote_hidden)

        # Sage ein Buchstabe
        buchstabe = input('Sage einen Buchstaben!')

        # Testen ob diesen Buchstaben gibt
        if buchstabe in quote:
            quote_hidden = reveal_letter_in_quote(buchstabe, quote, quote_hidden)

        else:
            leben -= 1
            print(f'Buchstaben nicht vorhanden! Du hast noch {leben}')

    if leben > 0:
        print(f'Du hast gewonnen mit {leben}!')
    else:
        print(f'Du hast verloren. \n Der Satz lautet {quote}!')
