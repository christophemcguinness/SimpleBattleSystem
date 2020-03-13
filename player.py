class player:
    def __init__(self):
        self.maxHealth = 100
        self.maxMagicPoints = 50
        self.health = 100
        self.magicPoints = 50
        self.attackSkill = 10
        self.speedSkill = 10
        self.defenceSkill = 10

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

