if __name__ == '__main__':

    input('Please think about a number between 1 and 100.\nPress enter when ready.')

    lower_bound = 0
    upper_bound = 101

    while True:
        guess = lower_bound+(upper_bound-lower_bound)//2

        correct = input(f'Is the number {guess}? y, smaller (-) or bigger (+) ')
        if correct == 'y':
            print('I found it!')
            break
        elif correct == '+':
            print(f'Ok, it is bigger than {guess}')
            lower_bound = guess
        else:
            print(f'Ok, it is smaller than {guess}')
            upper_bound = guess
