import random

from bases.practice.tic_tac_toe.grid import Grid
from bases.practice.tic_tac_toe.human import Human
from bases.practice.tic_tac_toe.player import Player


class Game:

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        # initialiser la grille de 3x3
        self.grid = Grid()
        self.current_player = self.ask_who_start()

    def ask_who_start(self):
        # on demande à l'utilisateur s'il veut commencer ou laisser l'ordinateur
        if isinstance(self.player1, Human):
            answer = None
            while answer not in ['1', '2']:
                answer = input('Which player shall start first? (1/2)')
            starting_player = int(answer)-1
        else:
            starting_player = random.randint(0, 2)
        return starting_player

    def start(self):
        print(f'New game between {self.player1.name} and {self.player2.name}')

        # tant que personne n'à gagné
        while self.grid.check_grid_result() is None:

            # on demande au joueur actuel son prochain coup
            if self.current_player == 0:
                index_line, index_col = self.player1.get_next_play(self.grid)
                if index_line == -1:
                    continue
                self.grid.cells[index_line][index_col] = self.player1.sign
            else:
                index_line, index_col = self.player2.get_next_play(self.grid)
                if index_line == -1:
                    continue
                self.grid.cells[index_line][index_col] = self.player2.sign

            # on affiche la grille
            print(self.grid)

            # on passe au joueur suivant
            if self.current_player == 0:
                self.current_player = 1
            else:
                self.current_player = 0

        # afficher le résultat
        result = self.grid.check_grid_result()
        if result is False:
            print('Draw! ')
        else:
            if result == self.player1.sign:
                print(f'{self.player1.name} won! ')
            else:
                print(f'{self.player2.name} won! ')

