import random

if __name__ == '__main__':

    continue_game = True

    while continue_game:

        leben = 2
        zahl = random.randint(0, 101)

        user_input = -1

        while user_input != zahl and leben != 0:

            print(f'Du hast noch {leben} Leben ')

            while True:
                user_input = input('Welche nummer?')

                if user_input.isdigit():
                    user_input = int(user_input)
                    break

            if zahl == user_input:
                print("You win!")
            elif zahl > user_input:
                print("Zahl ist grösser")
            else:
                print("Zahl ist kleiner")

            leben -= 1

            if leben == 0:
                print("You loose!")

        user_input_game = input('Möchten Sie weiterspielen? J/N')
        continue_game = 'j' in user_input_game.lower()
