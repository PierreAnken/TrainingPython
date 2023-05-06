def odds_in_range(min_value, max_value):

    if min_value % 2 == 0:
        min_value += 1

    return list(range(min_value, max_value + 1, 2))

def biggest_divisor(eingabenumber):
    for divisor in range(eingabenumber-1, 0, -1):
        if eingabenumber % divisor == 0:
            return divisor


print(biggest_divisor(99))
