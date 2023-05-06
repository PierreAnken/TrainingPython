import random

if __name__ == '__main__':

    # The player think about a number in his head (1-100)
    start_number = 1
    end_number = 100
    state_number = '-'

    # Until the computer has found the correct number
    while state_number != '=':

        state_number = '-'
        # Computer choose (wisely) a number
        number = random.randint(start_number, end_number)
        print(f'Der Computer hat die Zahl {number} gewählt')

        # Player tell the computer the result (><=) > => 'number to find is bigger'
        while state_number not in '<>=':
            state_number = input('Gebe ein > oder < oder = ein')

        # The computer has to update the range where he guess numbers
        if state_number == '>':

            start_number = number + 1
        elif state_number == '<':
            end_number = number - 1

    # When the game ended the computer write his result
    print('You I won!')