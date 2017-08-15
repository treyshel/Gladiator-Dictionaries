from random import randint, choice


def new_gladiator(health, rage, damage_low, damage_high):
    return {
        'health': health,
        'rage': rage,
        'damage low': damage_low,
        'damage high': damage_high
    }


def attack(attacker, defender):
    damage_dealt = randint(attacker['damage low'], attacker['damage high'])
    if randint(1, 100) <= attacker['rage']:
        defender['health'] -= (2 * damage_dealt)
        attacker['rage'] = 0
        message = '\nCRIT HIT OF {}'.format(damage_dealt)
    else:
        defender['health'] -= damage_dealt
        attacker['rage'] += 15
        message = '\nHIT OF {}'.format(damage_dealt)
    return message


def heal(gladiator):
    if gladiator['rage'] >= 10:
        gladiator['rage'] = max(gladiator['rage'] - 10, 0)
        gladiator['health'] = min(gladiator['health'] + 5, 100)


def is_dead(gladiator):
    if gladiator['health'] <= 0:
        return True
    return False


def rand_damage(damage_1, damage_2):
    damage_1 = randint(5, 25)
    damage_2 = randint(5, 25)
    return min(damage_1, damage_2), max(damage_1, damage_2)


def pass_turn(gladiator):
    gladiator['rage'] += 30
