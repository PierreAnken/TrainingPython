print('\nAufgabe 21.a')


def list_splitting(lst, split_index):
    lst1 = lst[:split_index]
    lst2 = lst[split_index:]
    return lst1, lst2


print(list_splitting([2, 4, 5, 1, 9], 3))
print(list_splitting([2, 4, 5, 1, 9], 6))

print('\nAufgabe 21.b')


def multiply(vals1, vals2):
    table = []
    for v1 in vals1:
        line = []
        for v2 in vals2:
            line.append(v1 * v2)
        table.append(line)
    return table


vals1 = [2, 5]
vals2 = [5, 6, 1]
print(multiply(vals1, vals2))
