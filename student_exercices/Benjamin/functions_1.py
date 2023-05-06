import random


def biggest_number(*numbers):
    saved_number = 0
    # for each number in numbers
    for number in numbers:
        # is the number > as saved number?
        if number > saved_number:
            # yes, overwrite saved number
            saved_number = number

    # return saved number
    return saved_number


def generate_numbers(anzahl_numbers):
    return random.sample(range(1, 101), anzahl_numbers)


print(biggest_number(*generate_numbers(10)))
