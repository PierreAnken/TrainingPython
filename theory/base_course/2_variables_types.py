# I'm a comment - indentation is important
print('I\'m printing inside the terminal. \tTabulation \nNew line')

# Attribute + Method call
print('hello world'.title())

# Assignation
var1 = 123
var2 = var1 + 2
print(var2)

# Multiple assignation
x, y, z = "Orange", "Banana", "Cherry"
a, b, c = ["Orange", "Banana", "Cherry"]
x, y = y, x

# Data type
print(' === data type === ')
my_string = 'abc'  # my_string = ['a', 'b', 'c']
print(my_string[0])

my_list = ['a', 'b', 'c']
print(my_list[0])

my_multiline_string = '''
SELECT *
FROM animals
WHERE age > 10
LIMIT 10;
'''

my_int = 1_000_000
my_float = 2.4
my_bool = True  # False

# Casting
print(' === casting === ')
hundred_as_str = '100'  # 100
print(type(hundred_as_str))

hundred_as_int = int(hundred_as_str)
print(type(hundred_as_int))
print(hundred_as_int + 5)

print(hundred_as_str + str(5) + ' abc')
print(5 * 'x')

# Structures
print(' === structures === ')
my_list = ['a', 5, 'test', 'toto', 7]
print(['abc'] * 5)

print(my_list)
empty_list = []  # list()

my_list[1] = 'dog'
print(my_list)

my_list.append(['a', 'b', 'c'])
print(my_list)

my_list.extend(['1', '2', '3'])
print(my_list)

my_list.insert(0, 'bird')
print(my_list)

print(' === tuple === ')
my_tuple = ('abc', 1, [1, 2, 3])
print(type(my_tuple), my_tuple[2][0])

print(' === set === ')
# set = no duplicates
my_set = {'a', 'a', 'b'}

empty_set = set()
print(my_set)
print(list(set([1, 1, 2, 3, 4])))

print(' === range === ')
my_range = range(1, 15, 2)  # [2, 4, 6, ..]
print(list(my_range))

print(' === dict === ')
empty_dict = {}
my_dict = {
    'key1': 'value1',
    2: [1, 2]
}

print(my_dict)
my_dict.update(
    {
        'key1': 11,
        'key3': 123
    }
)
print(my_dict)

my_dict['key4'] = 'abc'
print(my_dict)

del my_dict['key4']
print(my_dict)

print('key5', my_dict.get('key5', 'Nothing'))  # None
print('key1', my_dict.get('key1', 'Nothing2'))  # None

# print(my_dict['key5'])

print(list(my_dict.keys()))
