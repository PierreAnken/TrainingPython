import copy

from bases.practice.tic_tac_toe import grid
from bases.practice.tic_tac_toe.player import Player
import random


class AI(Player):
    def __init__(self, sign: str):
        ai_name = f'computer{random.randint(0, 1000)}'
        super().__init__(name=ai_name, sign=sign)

    def get_next_play(self, grid: Grid):

        # get all empty cells => [(index_line, index_col),(index_line, index_col)]
        empty_cells = []

        for index_line, line in enumerate(grid.cells):
            for index_cell, cell in enumerate(line):
                if grid.cells[index_line][index_cell] == ' ':
                    empty_cells.append((index_line, index_cell))

        # computer test if he can win with any move
        for empty_cell in empty_cells:
            grid_test = copy.deepcopy(grid)
            index_line, index_cell = empty_cell
            grid_test.cells[index_line][index_cell] = self.sign
            if grid_test.check_grid_result() == self.sign:
                print(f'{index_line+1}{index_cell+1} is wining!')
                return empty_cell

        # computer select a random empty cell
        print('No win found, random')
        return random.sample(empty_cells, 1)[0]
