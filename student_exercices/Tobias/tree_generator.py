#               *
#               +
#              + +
#            + + + +
#             =====
#            =======
#          o + + + o +
#           + + o o +
#          o + + + o +
#         o o + + + o +
#               |

#     Jede 5 Linien ist eine Linie breiter um 1, darf nicht die letzte Linie sein
import random


def get_width_row(height):
    # 2 => 3 / 3 => 5 / 4 => 7 / 5 => 9
    # double de la hauteur -1
    return height * 2 - 1


def compute_tree_row_space_left(tree_row, width_base):
    # (row width - tree width)/2
    tree_row_size = get_width_row(tree_row)
    return (width_base - tree_row_size) // 2


def generate_tree_row(row_number, width_base, thicker_row=False):
    space_left = compute_tree_row_space_left(row_number, width_base)
    space_str = space_left * ' '

    if random.randint(0, 100) > 70 and row_number > 3 and not thicker_row:
        tree_row_str = (row_number * '==')[:-1]
    else:
        tree_row_str = (row_number * '+ ')[:-1]
        tree_row_str = randomly_create_ball(tree_row_str)
    print(space_str + tree_row_str)

    if thicker_row:
        generate_tree_row(row_number+2, width_base)


def randomly_create_ball(tree_row_str):
    # + + +
    new_row_str = ''

    for element in tree_row_str:
        # add spaces
        if element == ' ':
            new_row_str += ' '
        # add ball or tree
        else:
            if random.randint(1, 100) > 80:
                new_row_str += 'o'
            else:
                new_row_str += '+'
    return new_row_str


def generate_tree_decoration(width_base, sign):
    space_left = compute_tree_row_space_left(1, width_base)
    space_str = space_left * ' '
    print(space_str + sign)


def generate_tree(height):

    if height < 2:
        return

    width_base = get_width_row(height)
    generate_tree_decoration(width_base=width_base, sign='*')
    for row_number in range(1, height + 1):
        thicker_row = False

        # create larger line
        if row_number % 3 == 0 and row_number != height:
            row_number += 1
            thicker_row = True

        generate_tree_row(row_number=row_number, width_base=width_base, thicker_row=thicker_row)
    generate_tree_decoration(width_base=width_base, sign='|')


if __name__ == '__main__':
    generate_tree(height=12)
