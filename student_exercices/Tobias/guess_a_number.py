import random

if __name__ == '__main__':

    # Computer wählt eine Zufallszahl zwischen 1 und 100
    computer_number = random.randint(1, 100)
    our_input = None
    user_try_number = 0

    # Das Spiel stoppt, sobald wir die richtige Zahl erraten haben
    while our_input != computer_number and user_try_number < 7:
        # Wir erhalten eine Eingabe und Raten
        user_try_number += 1

        our_input = ''
        while not our_input.isdigit():
            our_input = input(f"Please insert a number between 1 and 100. Remaining tries: {8-user_try_number}")
        our_input = int(our_input)

        # Wenn Eingabe nicht übereinstimmt, bekommen wir negative Rückmeldung
        if computer_number > our_input:
            print("The number to find is bigger!")
        elif computer_number < our_input:
            print("The number to find is smaller!")

    # Es wird überprüft ob die Eingabe mit der Computerzahl übereinstimmt
    # Wenn Eingabe übereinstimmt, bekommen wir positive Rückmeldung
    if computer_number == our_input:
        print("You won!")
    else:
        print(f"You lost! The number to find was: {computer_number}")