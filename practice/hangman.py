
import requests
from random import sample
import string


def get_quotes(url):
    # Make a GET request and get response data
    response = requests.get(url)

    # parse json and get the quote list back
    data = response.json()
    return data


def generate_hidden_quote(text):

    # replace all alphabetic signs with _
    for letter in string.ascii_letters:
        text = text.replace(letter, '_')

    # Return hidden quote
    return text


def show_letter(user_letter, quote_hidden, quote):

    if user_letter == '#':
        index_underscore = quote_hidden.find('_')
        user_letter = quote[index_underscore]

    for index, letter in enumerate(quote):
        if user_letter.lower() == letter.lower():
            # quote_hidden = text_before_letter + letter + text_after_letter
            # abc_ef_h => index = 3
            # abc + user_letter + ef_h
            quote_hidden = quote_hidden[:index]+letter+quote_hidden[index+1:]

    return quote_hidden


if __name__ == '__main__':

    # Get all quotes from api
    api_url = 'https://type.fit/api/quotes'
    all_quotes = get_quotes(api_url)

    # extract one quote text

    # print(type(all_quotes))
    # print(len(all_quotes))

    chosen_quote = sample(all_quotes, 1)
    # print(chosen_quote)

    dict_chosen_quote = chosen_quote[0]

    print(dict_chosen_quote)
    # print(type(dict_chosen_quote))

    chosen_quote_text = dict_chosen_quote.get('text')
    # print(chosen_quote_text)

    # generate hidden version of the quote
    hidden_quote = generate_hidden_quote(chosen_quote_text)
    print(hidden_quote)

    life_amount = 5
    asked_letter = []

    print('Game started. Input # to get as a joker letter.')

    # While life > 0 and not all letter have been found
    while life_amount > 0 and hidden_quote.count('_') > 0:
        # ask user for a letter
        chosen_letter = input('Choose a letter: ')

        if len(chosen_letter) != 1:
            print('Invalid input, please choose a letter')
            continue

        if chosen_letter in asked_letter:
            print('Letter or joker already asked, please choose another letter.')
            continue
        else:
            asked_letter.append(chosen_letter)

        # if letter not in quote, remove a life
        if chosen_quote_text.lower().count(chosen_letter.lower()) == 0 and chosen_letter != '#':
            life_amount -= 1
            print(f'{chosen_letter} is not in the quote. {life_amount} lives remaining.')

        # else display letter in hidden quote
        else:
            # display in hidden quote, the found letter
            hidden_quote = show_letter(chosen_letter, hidden_quote, chosen_quote_text)

        print(hidden_quote)

    # tell the user weather he won or lost
    if life_amount == 0:
        print(f'You lost! The quote was *{chosen_quote_text}*')
    else:
        print('You won!')
