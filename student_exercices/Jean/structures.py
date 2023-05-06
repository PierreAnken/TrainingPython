structure = (
    1,
    2,
    ['a', 'b', {
        'x': 23,
        'y': ('defg', ['hijk'])
    }]
)

print(structure, type(structure))
print(structure[2], type(structure[2]))
print(structure[2][2], type(structure[2][2]))
print(structure[2][2]['y'], type(structure[2][2]['y']))
print(structure[2][2]['y'][1], type(structure[2][2]['y'][1]))
print(structure[2][2]['y'][1][0], type(structure[2][2]['y'][1][0]))
print(structure[2][2]['y'][1][0][-1], type(structure[2][2]['y'][1][0][-1]))

texte = 'a,b,c,:1:2:3'
lettres = texte[0:6]
chiffres = texte[6:]
print(lettres, chiffres)

lettres_lst = lettres.split(',')[:-1]
chiffres_lst = chiffres.split(':')[1:]
print(lettres_lst, chiffres_lst)



