def some_function(lst, threshold):
    return sum(lst) < threshold


print(some_function([1, 2, 3], 7))
print(some_function([1, 2, 3], 2))
