def inverse(some_file):
    buffer = some_file[:]
    for valeur in buffer:
        some_file.pop()
        some_file.insert(0, valeur)


def invert(some_file, buffer):
    if some_file:
        buffer.insert(0, some_file.pop())
        invert(some_file, buffer)
        some_file.insert(0, buffer.pop(0))


file = [5, "bonjour", 8.35, True]
# inverse(file)
print(file)

invert(file, [])
print(file)