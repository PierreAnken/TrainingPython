from typing import Union
from student_exercices.Joël.TicTacToe.board import Board
from student_exercices.Joël.TicTacToe.sign import Sign
from student_exercices.Joël.TicTacToe.spieler import Spieler


class Game:



    def __init__(self):
        self.spieler1 = Spieler(Sign.o, 'Player 1')
        self.spieler2 = Spieler(Sign.x, 'Player 2')
        self.board = Board()
        self.current_player = self.spieler1

    def board_full(self):
        return self.board.is_full()

    def get_winner(self) -> Union[Spieler, None]:
        sign_winner = self.board.get_winning_sign()
        if sign_winner == self.spieler1.sign:
            return self.spieler1

        if sign_winner == self.spieler2.sign:
            return self.spieler2

        return None

    def display_result(self):

        # Der Gewinner aus der Methode get_winner wird in der Variable winner gespeichert
        winner = self.get_winner()
        # Ist winner gleich None ist Unentschieden
        if winner is None:
            print("Unentschieden!")

        # Ist winner nicht gleich None wird der Name des Winner ausgeben
        else:
            print(f"Herzlichen Glückwunsch {winner.name} hat gewonnen")

    def get_next_player(self) -> None:
        # Wenn der Spieler gleich ist wie Spieler 1 wechsle den Spieler zu Spieler2 sonst zu Spieler1
        if self.spieler1 == self.current_player:
            self.current_player = self.spieler2
        else:
            self.current_player = self.spieler1


    def play(self):

        # Das Spiel geht solange bis ein Spieler gewonnen hat oder das Board ist voll
        self.get_players_name()
        while not self.board_full() and not self.get_winner():
            next_move = self.get_next_move()
            # Klasse Board mit dem Objekt brett mit den Werten O und 2 aus der Variable next_move

            self.board.update_board(self.current_player.sign, position=next_move)
            #Print von Board
            print(self.board)

            self.get_next_player()

    def get_next_move(self) -> Union[tuple[int, int], None]:

        # (x,y)
        next_move_position = None

        while not next_move_position:
            next_move = input(f'{self.current_player.name} next move? [x,y] from top left')

            # check if text size == 3
            if len(next_move) == 3:
                # check if text [0] and [2] are numbers:
                if next_move[0].isdigit() and next_move[2].isdigit():

                    line, column = int(next_move[0]), int(next_move[2])

                    # check if the coordinates are in the board
                    if 1 <= line <= 3 and 1 <= column <= 3:

                        # check if board at position x,y == None
                        if not self.board.brett[line - 1][column - 1]:
                            next_move_position = (line - 1, column - 1)

        return next_move_position

    def get_players_name(self):
        #Methode zur Eingabe von Spielernamen
        self.spieler1.name = input('Wie heisst Spieler 1?')
        self.spieler2.name = input('Wie heisst Spieler 2?')
