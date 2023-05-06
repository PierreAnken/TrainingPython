import random

# man wählt eine nummer zwischen 1 und 100
random_number = random.randint(1, 100)
number_guessed = 0
tries = 7

# bis die nummer ist nicht gleich
while number_guessed != random_number and tries != 0:

    # man probiert die nummer zu erraten
    number_guessed = ''
    while not number_guessed.isdigit():
        number_guessed = input(f"Enter Number (1-100) / deine Vesuche: {tries} / 7 : ")

    number_guessed = int(number_guessed)

    tries -= 1

    if tries != 0:
        # falls die nummer ist gleich => hat der benuzer gewonnen
        if number_guessed > random_number:
            print("Nummer ist kleiner ")
        # falls die nummer ist kleiner => sagen die nummer ist kleiner
        elif number_guessed < random_number:
            print("Nummer ist grösser")

if number_guessed != random_number:
    print("Du hast verloren.")
# falls die nummer ist grosser => sagen: nummer ist grosser
else:
    print("Gewonnen!!!")
