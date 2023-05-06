from random import sample
import random

class Player:
    nicknames = ['Blacklight',
                 'OwlChick',
                 'CitarNosis',
                 'ThunderHawk',
                 'PowerGrab',
                 'Seismology',
                 'RichterScales',
                 'Palpebral',
                 'Maggotta',
                 'Myopia',
                 'MsMittens',
                 'Monstrum',
                 'PanzerElite',
                 'BatBoy',
                 'Slyrack']

    def __init__(self, active_tank, nickname=None):

        if not nickname:
            nickname = sample(self.nicknames, 1)[0]
            nickname = f'{nickname}_{random.randint(1, 100)}'

        self.active_tank = active_tank
        self.nickname = nickname

    def attack_other_team(self, other_team):
        player_targeted = self.select_target(other_team)
        if player_targeted:
            self.active_tank.inflict_damage(player_targeted.active_tank)

    def select_target(self, other_team):

        if type(other_team).__name__ != 'Team':
            raise ValueError('Other team is invalid')

        if not other_team.team_is_alive():
            return None

        # select only players with active tanks
        active_enemies = list(filter(lambda player: not player.active_tank.death, other_team.list_player))

        # arty are focused at the end
        arty_players = list(filter(lambda player: type(player.active_tank).__name__ == 'ArtyTank', active_enemies))
        non_arty_players = list(filter(lambda player: type(player.active_tank).__name__ != 'ArtyTank', active_enemies))

        if len(non_arty_players) != 0:
            target_player = sample(non_arty_players, 1)[0]
        else:
            target_player = sample(arty_players, 1)[0]

        return target_player
