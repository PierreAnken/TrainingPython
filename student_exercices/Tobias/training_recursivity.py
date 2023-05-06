from copy import copy


def reverse(list1, level, new_list):
    value = list1[0] if list1 else None

    if value is None:
        return

    list1 = list1[1:]
    reverse(list1, level - 1, new_list)
    new_list.append(value)


some_list = [1, 2, 3, 4]
new_list = []
reverse(some_list, 0, new_list)
print(new_list)
