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


def test_pass_turn():
    gladiator = {'health': 100, 'rage': 0, 'damage low': 12, 'damage high': 12}
    pass_turn(gladiator)
    expect = {'health': 100, 'rage': 30, 'damage low': 12, 'damage high': 12}
    assert gladiator == expect


def test_stab():
    gladiator = {'health': 10, 'rage': 0, 'damage low': 8, 'damage high': 8}
    stab(gladiator)
    expect = {'health': 0, 'rage': 0, 'damage low': 8, 'damage high': 8}
    assert gladiator == expect


def test_mega_kick():
    attacker = {'health': 100, 'rage': 60, 'damage low': 12, 'damage high': 12}
    defender = {'health': 45, 'rage': 10, 'damage low': 12, 'damage high': 12}
    mega_kick(attacker, defender)
    expect_attacker = {
        'health': 100,
        'rage': 0,
        'damage low': 12,
        'damage high': 12
    }
    expect_defender = {
        'health': 10,
        'rage': 10,
        'damage low': 12,
        'damage high': 12
    }
    assert attacker == expect_attacker
    assert defender == expect_defender
