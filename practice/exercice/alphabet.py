from string import ascii_lowercase as alphabet


def get_index_letter(given_letter):
    for counter, letter in enumerate(alphabet):
        if letter == given_letter:
            print(f'The letter {given_letter} is at the position {counter+1} from the alphabet')
            break


if __name__ == '__main__':
    user_input = input("Please enter a letter ")
    get_index_letter(user_input)
