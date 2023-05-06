# for i in range(3, 0, -1):  # [3,2,1]
#     print(i * "*")

# lst = [1, 2, 3, 4, 5]
# for i in range(1, len(lst)):  # [1,2,3,4]
#     lst[i] += lst[i - 1]
#     # lst[1] += lst[1 - 1] => [1, 3, 3, 4, 5]
#     # lst[2] += lst[2 - 1] => [1, 3, 6, 4, 5]
#     # lst[3] += lst[3 - 1] => [1, 3, 6, 10, 5]
#     # lst[4] += lst[4 - 1] => [1, 3, 6, 10, 15]
# print(lst)


# def list_mutation(lst):
#     for i in range(1, len(lst)):  # [1,2,3]
#         lst[i] = lst[i - 1] + lst[i]
#         # lst[1] = lst[1 - 1] + lst[1] => [1, 3, 3, 4]
#         # lst[2] = lst[2 - 1] + lst[2] => [1, 3, 6, 4]
#         # lst[3] = lst[3 - 1] + lst[3] => [1, 3, 6, 10]
# lst = [1, 2, 3, 4]
# list_mutation(lst)
# print(lst)


