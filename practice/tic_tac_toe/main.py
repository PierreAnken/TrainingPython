from bases.practice.tic_tac_toe.ai import AI
from bases.practice.tic_tac_toe.game import Game
from bases.practice.tic_tac_toe.human import Human

if __name__ == '__main__':

    answer1 = input('AI battle? A or Human vs AI? H: ')

    if answer1 == 'A':
        player1 = AI('x')
    else:
        player1 = Human('x')
    player2 = AI('o')

    # Tant que l'utilisateur veut continuer a jouer
    user_want_to_continue = True
    while user_want_to_continue:
        game = Game(player1=player1, player2=player2)
        game.start()

        answer = input('Do you want to start a new game? (Y/N) ')
        user_want_to_continue = answer in ['Y', 'y', '1']
    print('Bye bye!')

