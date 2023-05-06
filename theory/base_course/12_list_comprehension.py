from string import ascii_lowercase as alphabet

number_list = [n*2 for n in range(10)]
print(number_list)

number_set = {n*3 for n in range(10)}
print(number_set)

even_number_list = [n for n in range(10) if n % 2 == 0]
print(even_number_list)

number_list_5 = [n for n in range(60) if '5' in str(n)]
print(number_list_5)

alphabet_dict = {letter: counter for counter, letter in enumerate(alphabet[:3])}
print(alphabet_dict)
