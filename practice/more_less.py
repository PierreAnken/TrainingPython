import random
from datetime import datetime


def ask_user_mode():
    choices = {
        'easy 1': (10, 100),
        'normal 2': (7, 250),
        'hard 3': (6, 500)
    }

    game_mode = None

    while not game_mode:
        user_input = input(f'Choose game mode: {", ".join(choices.keys())} ?')

        for key in choices.keys():
            if user_input in key.split():
                game_mode = key
                break

    return choices[game_mode]


if __name__ == '__main__':

    lives, MAX_VALUE = ask_user_mode()

    random_number = random.randint(0, MAX_VALUE)
    guess = None

    start_time = datetime.now()

    # until user has not found the number
    while random_number != guess and lives > 0:

        # ask user for a guess
        user_value = input(f'{lives} lives remaining - Value? ')

        # check answer is a number
        if not user_value.isnumeric():
            print(f'{guess} is not a valid number.')
            continue

        # convert answer to int
        guess = int(user_value)

        if guess > random_number:
            print('The number is smaller.')
            lives -= 1

        elif guess < random_number:
            print('The number is bigger.')
            lives -= 1

    if lives > 0:
        # if guess is correct => won
        end_time = datetime.now()
        duration = end_time-start_time

        print(f'You won in {duration}!')
    else:
        print(f"You´ve lost, Number was:{random_number} ")
