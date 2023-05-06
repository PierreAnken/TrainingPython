import random


class BaseTank:

    def __init__(self, tank_data):

        self.death = False
        self.model = tank_data.get('short_name')
        self.nation = tank_data.get('nation')

        default_profile = tank_data.get('default_profile')
        self.armor_dict = default_profile.get('armor').get('hull')
        self.health = default_profile.get('hp')
        self.precision = round((1 - default_profile.get('gun').get('dispersion')) * 100) - 10

        ammo_list = default_profile.get('ammo')
        self.ammo_damage = None
        for ammo in ammo_list:
            if ammo.get('type') == 'ARMOR_PIERCING':
                self.ammo_damage = ammo.get('damage')[2]
                break
        if not self.ammo_damage:
            raise Exception('No ammo damage found for type Armor Piercing')

    def __str__(self):
        return f'''
        Nation: {self.nation}
        Model: {self.model}
        Type: {type(self).__name__}
        Armor: {self.armor_dict} 
        Health: {self.health} 
        Damage: {self.ammo_damage}
        Precision: {self.precision}'''

    def dodge(self):
        return False

    def inflict_damage(self, enemy_tank):
        result = None
        if not self.death:
            if random.randint(1, 100) >= self.precision:
                enemy_tank.receive_damage(self.ammo_damage)
                result = 'hit'
            else:
                result = 'miss!'
        return result

    def receive_damage(self, damage_amount):
        if not self.death:
            self.health -= damage_amount
            if self.health <= 0:
                self.death = True
