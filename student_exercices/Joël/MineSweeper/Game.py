from student_exercices.Joël.MineSweeper.FieldPosition import Mine
from student_exercices.Joël.MineSweeper.MineField import MineField
from string import ascii_uppercase as alphabet


class Game:

    def __init__(self):
        # Dictionary with difficult
        difficult_bombs = {
            "light": 5,
            "middle": 7,
            "hard": 10,
            "heavy": 12
        }

        # Ask for difficulty
        chosen_difficulty = None
        while chosen_difficulty not in difficult_bombs.keys():
            chosen_difficulty = input('Prompt the difficulty of the Game. "light", "middle", "hard" and "heavy"!')

        self.field = MineField(9, 9, difficult_bombs[chosen_difficulty])
        self.play()

    def play(self):

        # Until the game is not finished (win or lose)
        while self.field.remaining_empty_hidden_position() > 0:
            index_x, index_y, is_marked = self.ask_next_position()
            field_position = self.field.mine_field[index_x][index_y]

            if is_marked:
                self.field.mark_position(index_x, index_y)
            else:

                # If the position has a bomb
                if field_position.mine == Mine.BOMBE:
                    break

                # We reveal the position and neighbours
                self.field.reveal_position(index_x, index_y)

        if self.field.remaining_empty_hidden_position() == 0:
            print('You win!')
        else:
            print('You lost!')

        print(self.field.get_field_as_str(reveal_all=True))

    def ask_next_position(self):
        print(self.field)

        position_valid = False
        is_mark = False

        while not position_valid:
            choose_field = input('Wähle ein Feldposition? Bsp. A3 oder A3X (markieren)')

            # User want to mark the cell?
            if len(choose_field) == 3:
                if choose_field[-1] != 'X':
                    continue
                else:
                    is_mark = True
            elif len(choose_field) != 2:
                continue

            if not choose_field[0].upper() in alphabet or not choose_field[1].isdigit():
                continue

            # Line Letter position is < as field height
            if alphabet.index(choose_field[0]) > self.field.field_height - 1:
                continue

            # Column is < field width
            if 0 < int(choose_field[1]) > self.field.field_width:
                continue

            return alphabet.index(choose_field[0]), int(choose_field[1]) - 1, is_mark


if __name__ == '__main__':
    game = Game()
