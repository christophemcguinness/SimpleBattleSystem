from random import randint
from player import player
from Battle import Battle

main_player = player()

while True:

    print('\nPlayers Stats:')
    print('Health: {0}/{1}'.format(main_player.health, main_player.maxHealth))
    print('MP: : {0}/{1}'.format(main_player.magicPoints, main_player.maxMagicPoints))
    print('Attack: {0}'.format(main_player.attackSkill))
    print('Speed: {0}'.format(main_player.speedSkill))
    print('Defence: {0}\n'.format(main_player.defenceSkill))

    if randint(0, 100) > 80:
        Battle(main_player).grainExp()

    input('Type anything to end the turn.\n')
