import random
#
# print('\nSchleifen')
# # for und while
#
# for number in range(20):
#     if number % 4 == 0:
#         print(number)

number1 = random.randint(0, 50)
number2 = random.randint(0, 50)

ergebniss = str(number1 + number2)
antwort = ''
while ergebniss != antwort:
    antwort = input(f'{number1}+{number2}?')

