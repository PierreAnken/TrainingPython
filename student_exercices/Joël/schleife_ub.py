numbers = list(range(1, 6))
print(numbers)

for index_x, wert in enumerate(numbers):
    neue_wert = wert ** 2
    numbers[index_x] = neue_wert

print(numbers)

for index_x, wert in enumerate(numbers):
    if wert % 2 == 1:
        neue_wert = wert * 2
        numbers[index_x] = neue_wert

print(numbers)

for index_x, wert in enumerate(numbers):
    neue_wert = str(wert)[::-1]
    numbers[index_x] = neue_wert

print(numbers)

for index_x, wert in enumerate(numbers):
    neue_wert = 0
    for digit in wert:
        neue_wert += int(digit)
    numbers[index_x] = neue_wert

print(numbers)

for index_x, wert in enumerate(numbers):
    # 4 => 4444 / '4' * 4 => '4444'
    neue_wert = int(str(wert) * wert)
    numbers[index_x] = neue_wert

print(numbers)

for index_x, wert in enumerate(numbers):
    # 4 => 4444 / '4' * 4 => '4444'
    neue_wert = ''
    for index_digit, digit in enumerate(str(wert)):
        if index_digit % 2 == 1:
            neue_wert += '0'
        else:
            neue_wert += str(digit)
    numbers[index_x] = int(neue_wert)

print(numbers)
