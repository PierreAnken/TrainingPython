from copy import copy
from random import sample

from misc.py_tanks.player import Player


class Team:

    def __init__(self, name):
        self.name = name
        self.list_player = []

    def add_player(self, player):

        if player in self.list_player:
            raise ValueError('Player already team')

        if type(player) != Player:
            raise ValueError('Invalid player')

        self.list_player.append(player)

    def generate_players(self, team_size, tank_list):
        if team_size < 1 or team_size > 15:
            raise ValueError('invalid team size (1-15)')

        print(f'\nTeam {self.name} generated with {team_size} players')

        for i in range(1, team_size + 1):
            player_tank = copy(sample(tank_list, 1)[0])
            new_player = Player(player_tank)
            self.add_player(new_player)

            print(f' - {new_player.nickname} with tank { player_tank.model} ')

    def team_is_alive(self):
        return self.get_alive_tank_number() != 0

    def get_alive_tank_number(self):
        alive_tank = 0
        for player in self.list_player:
            if not player.active_tank.death:
                alive_tank += 1
        return alive_tank



