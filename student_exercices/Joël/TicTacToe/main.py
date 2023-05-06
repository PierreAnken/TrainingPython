from student_exercices.Joël.TicTacToe.board import Board
from student_exercices.Joël.TicTacToe.game import Game

if __name__ == '__main__':
    game = Game()
    board = Board()
    game.play()

    # TODO: display winner
    while True:
        game.display_result()
        board.new_board()
        game.play()
