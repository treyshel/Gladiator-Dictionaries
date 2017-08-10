def new_gladiator(health, rage, damage_low, damage_high):
    return {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }


# def attack(attacker, defender):


def is_dead(gladiator):
    if ['health'] <= 0:
        return True
    return False