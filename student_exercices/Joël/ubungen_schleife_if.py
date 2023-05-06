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


if __name__ == '__main__':
    api_url = 'https://type.fit/api/quotes'

    quote_list = get_quotes(api_url, 20)

    while True:
        # Ein Satz wälen
        quote = random.sample(quote_list, 1)[0]
        quote_hidden = get_hidden_quote(quote)
        print(quote, '\n', quote_hidden, sep='')

        # Anzahl Leben
        leben = 10

        while True:
            # Sage ein Buchstabe
            buchstabe = input('Sage einen Buchstaben!')
            #   # Fragen ob diesen Buchstaben gibt
            if buchstabe in 'quote':
                quote_hidden = quote.replace('_', buchstabe)
                print(quote_hidden)

            elif quote == quote_hidden:
                print(f'Du hast gewonnen mit {leben} \n Der Satz lautet {quote}!')
                quote = 0

            else:
                leben -= 1
                print(f'Buchstaben nicht vorhanden! Du hast noch {leben} \n {quote_hidden}')

        break
        # Zeige alle vorhandenen Buchstaben
        # Falls kein Buchstaben vorhabend ein Leben abziehen
        # Stop wenn alle Buchstaben erraten sind oder keine Leben mehr
        # Von vorne beginnen
