def fibo_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_rec(n - 1) + fibo_rec(n - 2)


print(fibo_rec(10))


def fibo(n):
    n_1 = 1
    n_2 = 0
    for _ in range(n - 1):
        n_1, n_2 = n_1 + n_2, n_1
        print(n_1)


fibo(10)
