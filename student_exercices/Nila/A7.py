def some_function(num):
    d3 = num % 3 == 0
    d5 = num % 5 == 0

    if not d3 and not d5:
        return num

    if d3 and d5:
        return 'Bizz-Buzz'

    if d3:
        return 'Bizz'

    if d5:
        return 'Buzz'


for i in range(1, 101):
    print(i, some_function(i))

