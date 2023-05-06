def add_5(some_int: int):
    some_int += 5
    return some_int


def add_list_5(list_int: []):
    list_int.append(5)
    return list_int


def add_tuple_5(some_tuple: tuple):
    new_tuple = some_tuple + (5,)
    return new_tuple


def add_string_5(some_str: str):
    some_str = some_str + '5'
    return some_str


def add_dict_5(some_dict: dict):
    some_dict[5] = some_dict[5] + 5
    return some_dict


if __name__ == '__main__':

    print('int is immutable')
    base_int = 5
    print(add_5(base_int))
    print(base_int)

    print('list is mutable')
    base_list = [1, 2]
    print(add_list_5(base_list))
    print(base_list)

    print('tuple is immutable')
    base_some_tuple = (1, 2)
    print(add_tuple_5(base_some_tuple))
    print(base_some_tuple)

    print('string is immutable')
    base_str = 'base_text'
    print(add_string_5(base_str))
    print(base_str)

    print('dict is mutable')
    base_dict = {5: 5}
    print(add_dict_5(base_dict))
    print(base_dict)
