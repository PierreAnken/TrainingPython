def quadrat(x):

    numbers = []
    for i in range(1, x + 1):
        number = i ** 2
        numbers.append(number)

    return numbers


print(quadrat(5))
