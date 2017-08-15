from core import *


def get_decision(glad):
    while True:
        s = input(
            '\nGladiator {}... What would you like to do?\n-- attack\n-- pass\n-- heal\n-- quit\n'.
            format(glad))
        if s in ['attack', 'pass', 'heal']:
            return s
        elif s == 'quit':
            exit()


def glad_1(gladiator_1):
    print(
        '\nGladiator 1 --> | {} HP | {} RAGE | {} DAMAGE LOW | {} DAMAGE HIGH |'.
        format(gladiator_1['health'], gladiator_1['rage'], gladiator_1[
            'damage low'], gladiator_1['damage high']))


def glad_2(gladiator_2):
    print(
        'Gladiator 2 --> | {} HP | {} RAGE | {} DAMAGE LOW | {} DAMAGE HIGH |'.
        format(gladiator_2['health'], gladiator_2['rage'], gladiator_2[
            'damage low'], gladiator_2['damage high']))


def main():
    min_hit_1, max_hit_1 = rand_damage(5, 25)
    min_hit_2, max_hit_2 = rand_damage(10, 20)
    gladiator_1 = new_gladiator(100, 0, min_hit_1, max_hit_1)
    gladiator_2 = new_gladiator(100, 0, min_hit_2, max_hit_2)
    while True:
        glad_1(gladiator_1)
        glad_2(gladiator_2)
        choice = get_decision('1')
        if choice == 'attack':
            print(attack(gladiator_1, gladiator_2))
            if is_dead(gladiator_2):
                glad_1(gladiator_1)
                glad_2(gladiator_2)
                print('\nWINNER: GLADIATOR 1\nLOSER: GLADIATOR 2')
                exit()
        elif choice == 'heal':
            heal(gladiator_1)
        elif choice == 'pass':
            pass_turn(gladiator_1)
        else:
            print('Invalid Choice.')
            break
        glad_1(gladiator_1)
        glad_2(gladiator_2)
        choice = get_decision('2')
        if choice == 'attack':
            print(attack(gladiator_2, gladiator_1))
            if is_dead(gladiator_1):
                glad_1(gladiator_1)
                glad_2(gladiator_2)
                print('\nWINNER: GLADIATOR 2\nLOSER: GLADIATOR 1')
                exit()
        elif choice == 'heal':
            heal(gladiator_2)
        elif choice == 'pass':
            pass_turn(gladiator_2)
        else:
            print('Invalid Choice.')
            break


if __name__ == '__main__':
    main()