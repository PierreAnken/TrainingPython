print('\nAufgabe 20.a')


def func(a: float, b: float):
    return (a ** 2 + b) / (b + 1)


print('\nAufgabe 20.b')


def compare_to(f1, f2):
    if f1 == f2:
        return 0
    if f1 > f2:
        return 1

    return -1


print('\nAufgabe 20.c')

lst = [1, 2, 3]


def reset_list(lst: list):
    for index in range(len(lst)):
        lst[index] = 0


reset_list(lst)
print(lst)

import statistics


# mean_std_dev
def mean_std_dev(data):
    return statistics.mean(data), statistics.stdev(data)


# normalize
def normalize(data, m, s):
    for i in range(len(data)):
        data[i] = (data[i] - m) / s


# fill_list
def fill_list():
    lst = []

    with open("data.txt", "r") as file:
        for line in file:
            lst.append(float(line.strip("\n")))

        return lst


print('\nAufgabe 20.da')
datas = fill_list()
print(datas)

print('\nAufgabe 20.db')
m, s = mean_std_dev(datas)

print('\nAufgabe 20.dc')
normalize(datas,m,s)


print('\nAufgabe 20.dd')
print(datas)