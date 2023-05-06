import copy
import random

base_board = (
    ['x', 'W', 'x', 'x'],
    ['x', '_', '_', 'x'],
    ['x', '_', 'W', '_'],
    ['B', '_', 'B', '_']
)

winning_board = (
    ['x', 'B', 'x', 'x'],
    ['x', '_', '_', 'x'],
    ['x', '_', 'B', '_'],
    ['W', '_', 'W', '_']
)


def get_board_code(current_board):
    code = ''
    for line in current_board:
        for value in line:
            code += value
    return code


winning_board_code = get_board_code(winning_board)


def get_knight_positions(current_board):
    knight_positions = []
    for x in range(4):
        for y in range(4):
            if current_board[x][y] in ('B', 'W'):
                knight_positions.append((x, y, current_board[x][y]))
    return knight_positions


def get_possible_moves(current_board):
    knights_moves = []
    for knight in get_knight_positions(current_board):
        knight_x, knight_y, color = knight
        all_moves = [
            # top
            (knight_x - 1, knight_y + 2),
            (knight_x + 1, knight_y + 2),
            # bottom
            (knight_x - 1, knight_y - 2),
            (knight_x + 1, knight_y - 2),
            # left
            (knight_x - 2, knight_y - 1),
            (knight_x - 2, knight_y + 1),
            # right
            (knight_x + 2, knight_y - 1),
            (knight_x + 2, knight_y + 1),
        ]

        possible_moves = list(filter(lambda m: 0 <= m[0] <= 3 and 0 <= m[1] <= 3 and current_board[m[0]][m[1]] == '_', all_moves))
        for move in possible_moves:
            dict_knight = {
                'color': color,
                'position': (knight_x, knight_y),
                'move': move
            }
            knights_moves.append(dict_knight)
    return knights_moves


def print_board(current_board):
    for x in current_board:
        print(x, end='\n')


def get_same_tested_position(code, positions):
    for tested_position in positions:
        level, board_code_tested = tested_position
        if code == board_code_tested:
            return tested_position


def explore_positions_recursive(current_board: tuple, tested_positions: [], moves_done: tuple, winning_branches: [], level):
    print(f'Current board, level: {level}')
    board_code = get_board_code(current_board)
    print_board(current_board)

    if level > 40:
        return

    # if win position we save it
    if board_code == winning_board_code:
        print('win position')
        winning_branches.append((level, moves_done))
        return

    # if already tested we mark the branch as dead
    same_position_tested = get_same_tested_position(board_code, tested_positions)

    if same_position_tested:
        if same_position_tested[0] > level:
            print(f'We find a shorter way to the tested position. Old: {same_position_tested[0]}, new {level}')
            tested_positions.remove(same_position_tested)
        else:
            print('already tested with less moves')
            return

    # mark the position as tested
    tested_positions.append((level, board_code))

    # we try all the moves from current position
    possible_moves = get_possible_moves(current_board)
    random.shuffle(possible_moves)
    print(f'Possible moves: {len(possible_moves)}\n')

    for move in possible_moves:
        print(f'Move tested: {move}\n')

        # create a board with the move
        new_board = list(copy.deepcopy(current_board))
        new_board[move['position'][0]][move['position'][1]] = '_'
        new_board[move['move'][0]][move['move'][1]] = move['color']
        new_board = tuple(new_board)

        # save the move
        new_moves_done = list(copy.deepcopy(moves_done))
        new_moves_done.append(move)
        new_moves_done = tuple(new_moves_done)

        explore_positions_recursive(new_board, tested_positions, new_moves_done, winning_branches, level + 1)


if __name__ == '__main__':

    branches = []
    explore_positions_recursive(base_board, [], tuple(), branches, 0)

    shortest = 50
    saved = None
    shortest_detail = {}

    for winning_branche in branches:
        count = shortest_detail.get(winning_branche[0], 0)
        count += 1
        shortest_detail[winning_branche[0]] = count
        if winning_branche[0] < shortest:
            saved = winning_branche
            shortest = winning_branche[0]

    print(shortest, shortest_detail, saved)

    # print(get_board_code(base_board))
