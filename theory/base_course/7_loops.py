from string import ascii_lowercase as alphabet

print('\nFor each')

for letter in alphabet[:3]:  # abc
    print(letter, end=' ')

print('\n\nFor each - enumerate')

for index, letter in enumerate(alphabet[:3]):
    print(index, letter, end=' ', sep='-')

print('\n\nFor i')

for letter_number in range(3):  # [0, 1, 2]
    # ['a','b', ...]
    print(alphabet[letter_number], end=' ')

print('\n\nWhile')

letter_number = 0
while letter_number < 3:
    print(alphabet[letter_number], end=' ')
    letter_number += 1

print('\n\nBreak')

for letter in alphabet:  # ['a','b', ..., 'z']
    print(letter, end=' ')
    if letter == 'c':
        break

print('\n\nElse')

for letter in alphabet:
    pass
else:
    print('The for loop did run on all elements')

print('\n\nContinue')

for letter_number in range(11):
    if letter_number % 2 == 1:
        continue
    print(alphabet[letter_number], end=' ')

print('\n\nLoop in loop')

for letter1 in 'abc':  # ['a','b','c']
    for letter2 in 'zxy':  # ['z','y','x']
        print(letter1, letter2, sep='/', end=' ')

print('\n\nZip')

word = 'sugus'
for letter_start, letter_end in zip(word, word[::-1]):
    if letter_start != letter_end:
        print(word, 'is not a palindrome')
        break
else:
    print(word, 'is a palindrome')
