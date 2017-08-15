from core import *


def test_new_gladiator():
    assert new_gladiator(100, 15, 0, 0) == {
        'health': 100,
        'rage': 15,
        'damage low': 0,
        'damage high': 0
    }
    assert new_gladiator(1, 2, 3, 4) == {
        'health': 1,
        'rage': 2,
        'damage low': 3,
        'damage high': 4
    }


def test_is_dead():
    gladiator = {'health': 0, 'rage': 0, 'damage low': 0, 'damage high': 0}
    assert is_dead(gladiator) == True
    gladiator = {'health': 100, 'rage': 0, 'damage low': 0, 'damage high': 0}
    assert is_dead(gladiator) == False


def test_heal():
    gladiator = {'health': 95, 'rage': 10, 'damage low': 0, 'damage high': 0}
    heal(gladiator)
    assert gladiator['health'] == 100 and gladiator['rage'] == 0
    gladiator = {'health': 100, 'rage': 10, 'damage low': 0, 'damage high': 0}
    assert gladiator['health'] == 100 and gladiator['rage'] == 10


def test_attack():
    attacker = {'health': 75, 'rage': 0, 'damage low': 10, 'damage high': 10}
    defender = {'health': 75, 'rage': 0, 'damage low': 11, 'damage high': 13}
    attack(attacker, defender)
    assert attacker['rage'] == 15
    assert defender['health'] == 65
    attacker = {'health': 75, 'rage': 100, 'damage low': 10, 'damage high': 10}
    defender = {'health': 65, 'rage': 100, 'damage low': 11, 'damage high': 13}
    attack(attacker, defender)
    assert attacker['rage'] == 0
    assert defender['health'] == 45
    attacker = {'health': 75, 'rage': 50, 'damage low': 10, 'damage high': 20}
    defender = {'health': 65, 'rage': 100, 'damage low': 11, 'damage high': 13}
    attack(attacker, defender)
    assert attacker['rage'] == 65 or attacker['rage'] == 0
    assert defender['health'] <= 55 and defender['health'] >= 25