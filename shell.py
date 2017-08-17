from core import *
from random import choice
import time


def get_decision(glad):
    while True:
        s = input(
            '\nGladiator {}... What would you like to do?\n\n-- [P]UNCH (random damage from your high and low damage)\n-- [C]UT (damage of 10 when opponent health <= 10)\n-- [M]EGA KICK (damage of 35 when rage >= 60)\n-- [S]KIP (gives you +30 rage)\n-- [H]EAL (15 rage? get +5 to your HP)\n-- [Q]UIT\n'.
            format(glad)).upper().strip()
        if s in ['P', 'C', 'M', 'S', 'H']:
            return s
        elif s == 'Q':
            print(
                '\nGladiator {} has quit. Come back\nwhen you want to fight like a man!'.
                format(glad))
            exit()
        print('Invalid Choice')


def glad_1(gladiator_1):
    print(
        '\nAlcapinine --> | {} HP | {} RAGE | {} DAMAGE LOW | {} DAMAGE HIGH |'.
        format(gladiator_1['health'], gladiator_1['rage'], gladiator_1[
            'damage low'], gladiator_1['damage high']))


def glad_2(gladiator_2):
    print(
        'Kapotacion --> | {} HP | {} RAGE | {} DAMAGE LOW | {} DAMAGE HIGH |'.
        format(gladiator_2['health'], gladiator_2['rage'], gladiator_2[
            'damage low'], gladiator_2['damage high']))


def available_computer_decision(attacker, defender):
    if defender['health'] <= 10:
        return choice(['P', 'S', 'C'])
    elif defender['health'] <= 10 and attacker['rage'] >= 15:
        return choice('P', 'H', 'S')
    elif attacker['health'] <= 95:
        return choice(['P', 'H', 'S'])
    elif attacker['health'] >= 60:
        return choice(['M'])
    else:
        return choice(['P'])


def one_player():
    min_hit_1, max_hit_1 = rand_damage(5, 25)
    min_hit_2, max_hit_2 = rand_damage(10, 20)
    gladiator_1 = new_gladiator(100, 0, min_hit_1, max_hit_1)
    gladiator_2 = new_gladiator(100, 0, min_hit_2, max_hit_2)

    glad_1(gladiator_1)
    glad_2(gladiator_2)

    while True:
        #actual user
        choice = get_decision('ALCAPININE')
        if choice == 'P':
            print(attack(gladiator_1, gladiator_2))
        elif choice == 'C':
            stab(gladiator_2)
        elif choice == 'M':
            mega_kick(gladiator_1, gladiator_2)
        elif choice == 'H':
            heal(gladiator_1)
            print('You have healed for +5')
        elif choice == 'S':
            pass_turn(gladiator_1)
            print('+30 RAGE')
        else:
            print('Invalid Choice.')
            break
        glad_1(gladiator_1)
        glad_2(gladiator_2)
        if is_dead(gladiator_2):
            print(
                '\nWINNER: (you) GLADIATOR ALCAPININE\nLOSER: GLADIATOR KAPOTACION'
            )
            exit()
        #computer
        print('\nYour opponent is attacking...')
        time.sleep(2.5)
        choice = available_computer_decision(gladiator_2, gladiator_1)
        if choice == 'P':
            print(attack(gladiator_2, gladiator_1))
        elif choice == 'C':
            stab(gladiator_1)
        elif choice == 'M':
            mega_kick(gladiator_2, gladiator_1)
        elif choice == 'H':
            heal(gladiator_2)
            print('\nHealed for +5')
        elif choice == 'S':
            pass_turn(gladiator_2)
            print('\n+30 RAGE')
        glad_1(gladiator_1)
        if is_dead(gladiator_1):
            print(
                '\nWINNER: GLADIATOR KAPOTACION\nLOSER: (you) GLADIATOR ALCAPININE'
            )
            exit()


def two_player():
    min_hit_1, max_hit_1 = rand_damage(5, 25)
    min_hit_2, max_hit_2 = rand_damage(10, 20)
    gladiator_1 = new_gladiator(100, 0, min_hit_1, max_hit_1)
    gladiator_2 = new_gladiator(100, 0, min_hit_2, max_hit_2)

    glad_1(gladiator_1)
    glad_2(gladiator_2)

    while True:
        # everything alcapinine
        choice = get_decision('Alcapinine')
        if choice == 'P':
            print(attack(gladiator_1, gladiator_2))
        elif choice == 'C':
            stab(gladiator_2)
        elif choice == 'M':
            mega_kick(gladiator_1, gladiator_2)
        elif choice == 'H':
            heal(gladiator_1)
            print('You have healed for +5')
        elif choice == 'S':
            pass_turn(gladiator_1)
            print('+30 RAGE')
        else:
            print('Invalid Choice.')
            break
        glad_1(gladiator_1)
        glad_2(gladiator_2)
        if is_dead(gladiator_2):
            print(
                '\nWINNER: GLADIATOR ALCAPININE\nLOSER: GLADIATOR KAPOTACION')
            exit()

        # everything kapotacion
        choice = get_decision('Kapotacion')
        if choice == 'P':
            print(attack(gladiator_2, gladiator_1))
        elif choice == 'C':
            stab(gladiator_1)
        elif choice == 'M':
            mega_kick(gladiator_2, gladiator_1)
        elif choice == 'H':
            heal(gladiator_2)
            print('You have healed for +5')
        elif choice == 'S':
            pass_turn(gladiator_2)
            print('+30 RAGE')
        else:
            print('Invalid Choice.')
            break
        glad_1(gladiator_1)
        glad_2(gladiator_2)
        if is_dead(gladiator_1):
            print(
                '\nWINNER: GLADIATOR KAPOTACION\nLOSER: GLADIATOR ALCAPININE')
            exit()


def main():
    while True:
        one_or_two_player = input(
            'Would you like to play [O]NE or [T]WO player?\n').upper().strip()
        if one_or_two_player == 'O':
            print(one_player())
            break
        elif one_or_two_player == 'T':
            print(two_player())
            break


if __name__ == '__main__':
    main()