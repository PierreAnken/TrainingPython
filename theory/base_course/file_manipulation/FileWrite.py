
# Write numbers between 1 and 10 in a file
with open(file='numbers_1_10.txt', mode='w') as file_pointer:
    numbers_as_text = ''
    for number in range(1, 11):  # [1, 2, 3, ... , 10]
        numbers_as_text += f'{number}\n'

    file_pointer.write(numbers_as_text)
