import random

print('\nAufgabe 19.a')


def do_something(a):
    pass


for x in range(1, 1001):
    do_something(x)

print('\nAufgabe 19.b')
values = [1, 2, 3, 4]

while len(values) > 0:
    index = random.randint(0, len(values)-1)
    print(values.pop(index))

print('\nAufgabe 19.c')
name = 'Nila'

for index in range(len(name)):
    print(f'{index} : {name[index]}')

print('\nAufgabe 19.d')
values = [1, 1]
for _ in range(10):
    values.append(values[-1]+values[-2])
print(values)