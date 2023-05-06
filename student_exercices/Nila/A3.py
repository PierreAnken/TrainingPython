def some_function(values):
    indexes = list(range(len(values)))
    print('A', indexes)

    print('B', values)
    for index in indexes:
        values[index] += 1

    print('C', values)
    print('D', sum(values))


some_function([1, 2, 3, 4, 5])
