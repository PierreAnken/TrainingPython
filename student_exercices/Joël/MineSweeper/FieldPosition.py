from enum import Enum


class FieldPosition:
    def __init__(self, mine, bomb_counter=0):
        self.mine = mine
        self.status = Status.HIDDEN
        self.bomb_counter = bomb_counter

    def __str__(self):
        return self.display_position()

    def __repr__(self):
        return self.display_position()

    def display_position(self, reveal_all=False):

        if not reveal_all:

            if self.status == Status.MARKED:
                return 'X'

            if self.status == Status.HIDDEN or self.mine == Mine.BOMBE:
                return '?'

            if self.status == Status.BOMB_COUNTER:
                return self.bomb_counter

        else:
            if self.mine == Mine.BOMBE:
                return 'B'

        if self.mine == Mine.LEER:
            return ' '


class Mine(Enum):
    BOMBE = 1
    LEER = 2


class Status(Enum):
    VISIBLE = 1
    HIDDEN = 2
    MARKED = 3
    BOMB_COUNTER = 4
