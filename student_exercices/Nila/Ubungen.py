list_1 = ['a', 'b', 'c']
print(list_1[1])

dict_1 = {
    'a': ['a', ['bcde'], 'f']
}

print(dict_1['a'][1][0][2])

struct = (
    1,
    2,
    ['a', 'b', {
        'x': 23,
        'y': ('defg', 'hijk')
    }]
)

print('Struct')
print(struct, type(struct).__name__)
print(struct[2], type(struct[2]).__name__)
print(struct[2][2], type(struct[2][2]).__name__)
print(struct[2][2]['y'], type(struct[2][2]['y']).__name__)
print(struct[2][2]['y'][1], type(struct[2][2]['y'][1]).__name__)
print(struct[2][2]['y'][1][1:3], type(struct[2][2]['y'][1][1:3]).__name__)

