from random import randint
from string import ascii_uppercase as alphabet
from student_exercices.Joël.MineSweeper.FieldPosition import Mine, FieldPosition, Status


class MineField:

    def __init__(self, field_width, field_height, amount_bombs_perc):
        self.field_width = field_width
        self.field_height = field_height
        self.mine_field = self.init_field()
        self.place_bombs(amount_bombs_perc)
        self.compute_bomb_counter()

    def init_field(self):

        field = []

        # für jede linie
        for _ in range(self.field_width):
            # neue liste erfassen
            new_line = []
            # für jede "mine"
            for _ in range(self.field_height):
                # neue empty "mine" in linie liste einfugen
                new_line.append(FieldPosition(Mine.LEER))

            # linie liste in field einfugen
            field.append(new_line)

        return field

    def remaining_empty_hidden_position(self):
        counter = 0
        for line in self.mine_field:
            for field_postion in line:
                if field_postion.mine == Mine.LEER and field_postion.status == Status.HIDDEN:
                    counter += 1
        return counter

    def reveal_position(self, index_x, index_y, full_display=True):
        field_position = self.mine_field[index_x][index_y]

        # If we need to display the empty cell (no bomb nearby or user clicked on it)
        if full_display or field_position.bomb_counter == 0:
            field_position.status = Status.VISIBLE
            self.reveal_neighbour_cells(index_x, index_y)

        # Display amount of nearby bombs
        else:
            field_position.status = Status.BOMB_COUNTER

    def mark_position(self, index_x, index_y):
        field_position = self.mine_field[index_x][index_y]

        if field_position.status == Status.HIDDEN:
            field_position.status = Status.MARKED
        elif field_position.status == Status.MARKED:
            field_position.status = Status.VISIBLE

        # Display amount of nearby bombs
        else:
            field_position.status = Status.BOMB_COUNTER

    def reveal_neighbour_cells(self, index_x, index_y):
        for neighbour_position in self.get_neighbours_position(index_x, index_y, False):
            neighbour_field_position = self.mine_field[neighbour_position[0]][neighbour_position[1]]
            if neighbour_field_position.status == Status.HIDDEN:
                self.reveal_position(neighbour_position[0], neighbour_position[1], False)

    def get_amount_nearby_bombs(self, index_x, index_y):
        neighbours_cells = self.get_neighbours_position(index_x, index_y)
        bomb_count = 0
        for field_postion in neighbours_cells:
            if field_postion[2].mine == Mine.BOMBE:
                bomb_count += 1
        return bomb_count

    def compute_bomb_counter(self):
        for index_x, line in enumerate(self.mine_field):
            for index_y, field_postion in enumerate(line):
                self.mine_field[index_x][index_y].bomb_counter = self.get_amount_nearby_bombs(index_x, index_y)

    def get_neighbours_position(self, index_x, index_y, edges=True):

        # Ex. If Y = (5,5) they tested if all neighbours have a bomb
        # => From (4,4) to (6,6) the whole square is checked

        # (4,6) (5,6) (6,6)
        # (4,5) (uns) (6,5)
        # (4,4) (5,4) (6,4)

        # X X X
        # X Y X
        # X X X

        field_positions = []

        for pos_x in range(index_x - 1, index_x + 2):
            for pos_y in range(index_y - 1, index_y + 2):

                if not edges:
                    # top left
                    if pos_x == index_x - 1 and pos_y == index_y - 1:
                        continue

                    # top right
                    elif pos_x == index_x + 1 and pos_y == index_y - 1:
                        continue

                    # bottom left
                    elif pos_x == index_x - 1 and pos_y == index_y + 1:
                        continue

                    # bottom right
                    elif pos_x == index_x + 1 and pos_y == index_y + 1:
                        continue

                # not the base position
                if pos_x != index_x or pos_y != index_y:
                    if 0 <= pos_x < self.field_width and 0 <= pos_y < self.field_height:
                        field_positions.append((pos_x, pos_y, self.mine_field[pos_x][pos_y]))

        return field_positions

    def place_bombs(self, amount_bombs_perc):

        # Give the number of bombs
        bombs_to_place = int(amount_bombs_perc / 100 * self.field_width * self.field_height)

        # Until we placed all the bombes
        while bombs_to_place > 0:

            # random postion für die neue Bombe
            position_x = randint(0, self.field_width - 1)
            position_y = randint(0, self.field_height - 1)

            # Ist die Zelle leer platzieren wir eine Bombe
            if self.mine_field[position_x][position_y].mine is Mine.LEER:
                self.mine_field[position_x][position_y] = FieldPosition(Mine.BOMBE)
                bombs_to_place -= 1

    def __str__(self):
        return self.get_field_as_str()

    def get_field_as_str(self, reveal_all=False):
        #    1  2  3
        # 1  ?  ?  ?
        # 2  ?  ?  ?
        # 3  ?  ?  ?

        field_str = '    '

        # column headers
        for zahl in range(1, self.field_width + 1):
            field_str += str(zahl) + ' '

        field_str += '\n'

        # for each line
        for line_nbr, line_lst in enumerate(self.mine_field):

            field_str += f'\n {alphabet[line_nbr]}  '

            # for each element
            for field_position in line_lst:
                field_str += f'{field_position.display_position(reveal_all)} '

        return field_str
