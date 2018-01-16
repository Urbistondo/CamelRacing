import random
import _thread
import threading

from camel import CamelFactory
from race import Race


def start():
    print("Welcome to Camel Races")
    number_camels = int(input("Please choose the number of camels that will participate in the race (at least 2)\n"))
    print('Choose one of the following terrain types:')
    print('1. Sand')
    print('2. Grass')
    print('3. Mud')
    terrain = input()
    total_distance = int(input("Please enter the distance of the race\n"))
    step_distance = int(input("Please enter the distance the camels move each turn\n"))
    camels = list()
    camel_types = ['BactrianCamel', 'DomesticCamel', 'Dromedary']
    for i in range(number_camels):
        camels.append(CamelFactory.get_camel(random.choice(camel_types), i))
    run(camels, terrain, total_distance, step_distance)


def prompt_user(code):
    user_input = ""


def run(camels, terrain, total_distance, step_distance):
    user_camel = camels[0]
    race = Race(camels, terrain, total_distance, step_distance)

    while not race.is_finished():
        code = 'AXZ'
        try:
            timer = threading.Timer(5, _thread.interrupt_main)
            timer.start()
            user_input = input('%s\n' % code)
        except KeyboardInterrupt:
            print('NIIGGA WTF')
        timer.cancel()

        if user_input == '%s%s' % (code, code[::-1]):
            user_camel.move(step_distance)
        elif user_input == code:
            user_camel.move(step_distance / 2)
        else:
            print("Your camel didn't move!")


start()
