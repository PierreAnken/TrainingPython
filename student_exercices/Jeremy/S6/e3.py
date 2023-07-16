def table_multiplication(mul, bornInf, bornSup):
    for i in range(bornInf, bornSup + 1):
        print(mul, '*', i, '=', mul * i)


table_multiplication(10, 0, 10)
