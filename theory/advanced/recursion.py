# https://en.wikipedia.org/wiki/Fibonacci_number

def fibo(n):
    if n <= 0:
        return 0

    if n == 1:
        return 1

    fn_m1 = 0
    fn = 1

    for _ in range(n - 1):
        fn_m1, fn = fn, fn_m1 + fn  # [0 1 , 1 1 , 1 2 , 2 3 , 3 5 ]

    return fn


def fibo_recursive(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibo_recursive(n - 2) + fibo_recursive(n - 1)


if __name__ == '__main__':
    print(fibo(12))
    print(fibo_recursive(30))
