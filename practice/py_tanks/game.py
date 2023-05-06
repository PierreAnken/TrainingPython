
from misc.py_tanks.tanks.tank_factory import TankFactory
from misc.py_tanks.team import Team


class Game:

    def __init__(self):

        # get tank list from API
        factory = TankFactory()
        factory.load_tanks_from_api(1)

        # Generate team 1 and team 2
        self.team_1 = Team('Great Conqueror')
        self.team_2 = Team('Panzer Elite')

        self.team_1.generate_players(15, factory.get_tank_list())
        self.team_2.generate_players(15, factory.get_tank_list())

    def start_fight(self):
        print('\n')
        while self.team_1.team_is_alive() and self.team_2.team_is_alive():
            for player_team1, player_team2 in zip(self.team_1.list_player, self.team_2.list_player):
                player_team1.attack_other_team(self.team_2)
                player_team2.attack_other_team(self.team_1)

    def result_fight(self):
        if self.team_1.team_is_alive():
            print(f'\nVictory from {self.team_1.name}, remaining tanks {self.team_1.get_alive_tank_number()}')
        elif self.team_2.team_is_alive():
            print(f'\nVictory from {self.team_2.name}, remaining tanks {self.team_2.get_alive_tank_number()}')
        else:
            print(f'\nDraw {self.team_1.get_alive_tank_number()} / {self.team_2.get_alive_tank_number()}!')

