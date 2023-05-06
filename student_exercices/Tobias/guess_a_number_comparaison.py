# Wir definieren eine Zahl zwischen 1 und 100 in unserem kopf
import random

results_middle = [0 for _ in range(1, 100)]
results_random = [0 for _ in range(1, 100)]
for _ in range(1_000_000):

    number_to_find = random.randint(1, 100)
    computer_number = -1
    min_range = 1
    max_range = 100
    tries = 0

    # Wiederholt sich bis Bedingung erfüllt oder keine Leben mehr
    while number_to_find != computer_number:
        tries += 1
        # Der Computer rät eine beliebige Zahl zwischen min_range und max_range
        computer_number = min_range + (max_range - min_range) // 2

        # Der Computer bekommt auf Basis unserer Eingabe eine Rückmeldung ob die Zahl kleiner oder größer ist '<>='
        if computer_number > number_to_find:
            max_range = computer_number - 1
        elif computer_number < number_to_find:
            min_range = computer_number + 1

        elif computer_number == number_to_find:
            results_middle[tries-1] = results_middle[tries-1] + 1

    min_range = 1
    max_range = 100
    computer_number = -1
    tries = 0

    # Wiederholt sich bis Bedingung erfüllt oder keine Leben mehr
    while number_to_find != computer_number:
        tries += 1
        # Der Computer rät eine beliebige Zahl zwischen min_range und max_range
        computer_number = random.randint(min_range, max_range)

        # Der Computer bekommt auf Basis unserer Eingabe eine Rückmeldung ob die Zahl kleiner oder größer ist '<>='
        if computer_number > number_to_find:
            max_range = computer_number - 1
        elif computer_number < number_to_find:
            min_range = computer_number + 1
        elif computer_number == number_to_find:
            results_random[tries-1] = results_random[tries-1] + 1

print('Results with middle:', results_middle)
print('Results with random:', results_random)
