
from string import ascii_lowercase as alphabet, digits as numbers


# create the main
if __name__ == '__main__':

    # ask the user for a sentence
    user_sentence = input("Please write a sentence: ")

    # Compute with a loop, the amount of letters from the sentence (don't count the spaces!)
    # Exemple: "my little house" => 13

    amount_letter = 0
    amount_space = 0
    amount_numbers = 0

    for letter in user_sentence:
        if letter.lower() in alphabet:
            amount_letter += 1
        elif letter == ' ':
            amount_space += 1
        elif letter in numbers:
            amount_numbers += 1

    # compute the amount of punctuation
    amount_punctuation = len(user_sentence) - amount_letter - amount_space - amount_numbers

    # print "The sentence <> contains <> letters
    print(f"The sentence *{user_sentence}* contains {amount_letter} letters, {amount_space} spaces, {amount_punctuation} punctuation and {amount_numbers} numbers")

