import random



def print_random_number_0_x(x: int) -> None:
    """
    This function print a random number in range [0,x]
    """
    print('Print inside function:', random.randint(0, x))


def print_random_number_0_9() -> None:
    """
    This function print a random number in range [0,9]
    """
    print_random_number_0_x(9)


def get_random_number_0_x(x: int) -> int:
    """
    This function return a random number in range [0,x]
    """
    return random.randint(0, x)


def get_random_number_0_9() -> int:
    """
    This function return a random number in range [0,10]
    """
    return get_random_number_0_x(9)


def get_random_number_0_x_optional(x: int = 20) -> int:
    """
    This function return a random number in range [0,x] or [0,20] if x is not given
    """
    return get_random_number_0_x(x)


def get_sum(*values) -> int:
    """
    This function return a random value from a list of parameters
    """
    total = 0
    for value in values:
        total += value

    return total


def args_and_kwargs(*positional_arguments, **keyword_arguments):
    """
    Return the given arguments
    """
    return [type(positional_arguments), positional_arguments, type(keyword_arguments), keyword_arguments]


if __name__ == '__main__':

    param = 20

    # No return, one parameter
    print("\n == No return, one parameter == ")
    print('Param:', param, 'Return:', print_random_number_0_x(param))

    # No return no parameter
    print("\n == No return, no parameter == ")
    print('Return:', print_random_number_0_9())

    # Return, with one parameter
    print("\n == Return, with one parameter == ")
    print('Param:', param, 'Return:', get_random_number_0_x(param))

    # Return, without parameter
    print("\n == Return, without parameter == ")
    print('Return:', get_random_number_0_9())

    # Optional parameter
    print("\n == Optional parameter == ")
    print('Return:', get_random_number_0_x_optional())

    # Undefined amount of parameter
    print("\n == Undefined amount of parameter == ")
    print('Return:', get_sum(1, 2, 3, 4))

    # args kwargs
    print("\n == Args kwargs == ")
    print('Return:', args_and_kwargs(1, 2, 3, 4, v1='a', v2='c', v3='x'))
