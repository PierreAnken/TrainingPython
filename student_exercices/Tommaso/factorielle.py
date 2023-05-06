def print_rec_tree(node):
    print(node['val'])
    if 'gauche' in node.keys():
        print_rec_tree(node['gauche'])
    if 'droite' in node.keys():
        print_rec_tree(node['droite'])



arbre = {
    'val': [1, 10],
    'gauche': {
        'val': [2, 5],
        'gauche': {
            'val':
                [3, 4],

        },
    },
    'droite': {
        'val': [6, 9],
        'droite': {
            'val': [7, 8],
        }
    }
}
print_rec_tree(arbre)


