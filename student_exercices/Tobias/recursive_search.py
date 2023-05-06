def search(gesuchte_number, number_tpl):
    start = 0
    end = len(number_tpl) - 1

    while True:
        middle = (end - start) // 2
        if gesuchte_number == number_tpl[middle]:
            return middle
        elif gesuchte_number < number_tpl[middle]:
            end = middle - 1
        elif gesuchte_number > number_tpl[middle]:
            start = middle + 1


def search_recursive(gesuchte_number, number_tpl):
    start = 0
    end = len(number_tpl) - 1
    middle = end - start // 2

    # End
    if gesuchte_number == number_tpl[middle]:
        return middle

    elif gesuchte_number < number_tpl[middle]:
        return search_recursive(gesuchte_number, number_tpl[:middle - 1])
    elif gesuchte_number < number_tpl[middle]:
        return search_recursive(gesuchte_number, number_tpl[middle + 1:])


if __name__ == '__main__':
    numbers = (2, 5, 8, 12, 15)

    print(search(2, numbers))
    print(search_recursive(2, numbers))
