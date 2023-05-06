print('\nAufgabe 17.a')


def a(string):
    string2 = ''

    for letter in string:
        if letter.isupper():
            string2 += letter.lower()
        elif letter == "c":
            string2 += 'k'
        else:
            string2 += letter
    return string2


str_a = 'AbCdcc123'
print(a(str_a))

print('\nAufgabe 17.b')


def dataContains(searchString):
    with open('data.txt', 'r') as file_pointer:
        data = file_pointer.read()
        return searchString in data


print(dataContains('Dog'))
print(dataContains('Turtle'))

print('\nAufgabe 17.c')


def c(matrix):
    maximum = 0
    for line in matrix:
        for wert in line:
            if wert > maximum:
                maximum = wert

    return maximum


m = [
    [1, 88, 4],
    [22, 78, 55],
    [44, 28, 11]
]
print(c(m))
