# def get_even_numbers(min_value: int, max_value:int) -> list[int]:
#
#     even_values_list = []
#
#     if min_value % 2 == 0:
#         start_value = min_value
#     else:
#         start_value = min_value + 1
#
#     if max_value % 2 == 0:
#         end_value = max_value
#     else:
#         end_value = max_value + 1
#
#     for i in range(start_value, end_value+1, 2):
#         even_values_list.append(i)
#
#     return even_values_list


def get_even_numbers(min_value: int, max_value: int) -> list[int]:
    return list(filter(lambda x: x % 2 == 0, range(min_value, max_value + 1)))


def sort_values(values: list) -> list:
    values.sort(key=lambda x: int(x))
    return values


def sort_by_size(values: list) -> list:
    values.sort(key=lambda x: len(x))
    return values


def compute(operator: str, *numbers) -> int:
    result = None

    if operator == '+':
        result = sum(numbers)
    elif operator == '*':
        result = 1
        for x in numbers:
            result = result * x

    return result


if __name__ == '__main__':
    result_1 = get_even_numbers(min_value=8, max_value=20)
    print(result_1)  # [6, 8 ,10 ,12 ,14 ,16 ,18 ,20]

    result_2 = sort_values(values=['4', '11', '20', '3'])
    print(result_2)  # ['3', '4', '11', '20']

    result_3 = sort_by_size(values=['int', 'else', 'if', 'while'])
    print(result_3)  # ['if', 'int', 'else', 'while']

    result_4 = compute('+', 1, 2, 3)
    result_5 = compute('*', 2, 3)
    print(result_4 + result_5)  # 12
