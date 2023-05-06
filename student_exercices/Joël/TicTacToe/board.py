from copy import copy
from typing import Union

from student_exercices.Joël.TicTacToe.sign import Sign


class Board:
    _default_board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

    def __init__(self, board_position=None):
        if board_position:
            self.brett = board_position
        else:
            self.brett = copy(self._default_board)

    def __str__(self):
        str2print = "-------------\n"
        # Solange Zeile in self.brett dann solange sign in zeile
        for zeile in self.brett:
            str2print += "|"
            for sign in zeile:
                # Wenn sign gleich None zum str2print str2add hinzufügen sonst str2add und sign.name hinzfügen
                if type(sign) is Sign:
                    str2add = " " + sign.name + " |"
                else:
                    str2add = "   |"
                str2print = str2print + str2add
            # Zeilenumbruch und Line mit Zeichenumbruch
            str2print = str2print + "\n"
            str2print = str2print + "-------------\n"

        return str2print

    def update_board(self, sign, position):
        # Brett laden
        current_board = self.brett
        # Zeile die geändert werden muss
        row_to_change = current_board[position[0]]
        # sign updated row_to_change in der Tulpe auf der Postion 1
        row_to_change[position[1]] = sign
        # row_to_change updated current_board in der Tulpe auf der Postion 0
        current_board[position[0]] = row_to_change
        # current_board gib in self.brett
        self.brett = current_board
        # Rückgabe vom Wert self.brett
        return self.brett

    # Board is full, wenn line im brett und wert in line gleich None ist, gibt es False zurück wenn nicht True
    def is_full(self) -> bool:
        for line in self.brett:
            for wert in line:
                if wert is None:
                    return False
        return True

    def new_board(self):
        # if Board is full the set Board to default Board for a new Game
        if self.is_full is True:
            self.brett = self._default_board
            return self.brett

    def get_winning_sign(self) -> Union[Sign, None]:

        winning_sign = None

        # Board indexes
        # [00] [01] [02]
        # [10] [11] [12]
        # [20] [21] [22]

        wining_positions = [
            [(0, 0), (0, 1), (0, 2)],  # First line
            [(1, 0), (1, 1), (1, 2)],  # Second line
            [(2, 0), (2, 1), (2, 2)],  # Third line
            [(0, 0), (1, 0), (2, 0)],  # First column
            [(0, 1), (1, 1), (2, 1)],  # Second column
            [(0, 2), (1, 2), (2, 2)],  # Third column
            [(0, 2), (1, 1), (2, 0)],  # Diagonal top right
            [(0, 0), (1, 1), (2, 2)],  # Diagonal top left
        ]

        for wining_position in wining_positions:
            # [(0, 0), (0, 1), (0, 1)]
            cell_1, cell_2, cell_3 = wining_position

            if self.brett[cell_1[0]][cell_1[1]] == self.brett[cell_2[0]][cell_2[1]] == self.brett[cell_3[0]][cell_3[1]]:
                # Check if cells != None
                if self.brett[cell_1[0]][cell_1[1]]:
                    winning_sign = self.brett[cell_1[0]][cell_1[1]]
                    break

        return winning_sign
