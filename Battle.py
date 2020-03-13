from random import randint


class Battle:
    def __init__(self, main_player):
        self.temp_player = main_player

    def grainExp(self):
        self.temp_player.maxHealth = (self.temp_player.maxHealth + randint(0, 10))
        self.temp_player.maxMagicPoints = (self.temp_player.maxMagicPoints + randint(0, 10))
        self.temp_player.attackSkill = (self.temp_player.attackSkill + randint(0, 3))
        self.temp_player.speedSkill = (self.temp_player.speedSkill + randint(0, 3))
        self.temp_player.defenceSkill = (self.temp_player.defenceSkill + randint(0, 3))

    def ReturnNewPlayerObject(self):
        return self.temp_player
