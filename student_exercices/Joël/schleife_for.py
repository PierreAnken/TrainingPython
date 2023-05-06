liste_a = ['a', 'b', 'c', 'd']

for buchstabe in liste_a:
    print(buchstabe)

counter = 0
for _ in range(10):
    counter += 1
print(counter)

for letter_index in range(len(liste_a)):
    if liste_a[letter_index] == 'c':
        liste_a[letter_index] = ''
print(liste_a)

for letter_index, buchstabe in enumerate(liste_a):
    print(letter_index, buchstabe)

