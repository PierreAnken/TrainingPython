min_number = 1
max_number = 100
feedback = ''

# Until the computer found the right number
while feedback != '=':

    # The computer guess a number
    print('Debug:', min_number, max_number)

    # 1 - 100 => 1+99/2 => 50
    # 50 - 60 => 50 + 10/2 => 55
    guess = min_number + (max_number - min_number) // 2

    feedback = ''
    while feedback not in ['+', '-', '=']:
        feedback = input(f"KI: Ich haber geraten {guess}, ist es richtig?  (Guess ist +,-,=)")

    # If => receive a feedback on the direction (< oder >)
    if feedback == '+':
        max_number = guess - 1
    else:
        min_number = guess + 1
