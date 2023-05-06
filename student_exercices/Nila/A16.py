# a
def a():
    antwort = int(input("ein zahl eigeben"))
    for value in range(0, antwort + 1):
        if value % 2 == 0:
            print(value)


a()


# b
def b(x):
    return list(range(1, x + 1))


print(b(5))


# c

def c(lst, value):
    if value not in lst:
        lst.append(value)


liste_c = [1, 4, 5]
c(liste_c, 4)
print(liste_c)
c(liste_c, 6)
print(liste_c)
