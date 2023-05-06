# Wir definieren eine Zahl zwischen 1 und 100 in unserem kopf

life_number = 7
user_feedback = ''
min_range = 1
max_range = 100

# Wiederholt sich bis Bedingung erfüllt oder keine Leben mehr
while user_feedback != "=" and life_number != 0:
    # Der Computer rät eine beliebige Zahl zwischen min_range und max_range
    life_number -= 1
    computer_number = min_range + (max_range - min_range) // 2

    # Der Computer bekommt auf Basis unserer Eingabe eine Rückmeldung ob die Zahl kleiner oder größer ist '<>='
    user_feedback = input(f"Remaining tries: {life_number + 1}. Ist die Zahl {computer_number} ? (<>=): ")
    if user_feedback == "<":
        max_range = computer_number - 1
    elif user_feedback == ">":
        min_range = computer_number + 1

# Rückmeldung erfolgt, entweder Spiel gewonnen oder Spiel verloren
if user_feedback == "=":
    print("I won !!!!!")
else:
    answer = input(f'I lost :-(, what was the answer?')
    print(f"Ho I see, I was not so far away from {answer} ...")

# Wenn Spiel verloren, dann Eingabe der Nummer
# Computer gibt eine Rückmeldung - in beiden Fällen
