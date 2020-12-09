import random
import json

players_count = int(input('Введите кол-во игроков: '))
health_list = list(open('/Users/manager/PycharmProjects/bunker/cards/health.txt'))


def prepare_list(abstract_list):
    prepared_list = [i.strip("\n") for i in abstract_list]
    return prepared_list


def get_bunker():
    with open('/Users/manager/PycharmProjects/bunker/cards/accident.json', 'r', encoding='utf-8') as f:
        accident_list = json.load(f)
    return random.choice(accident_list)


def get_characteristic(characteristic):
    characteristic
    random_index = random.randint(0, len(health_list) - 1)
    return health_list.pop(random_index)


def create_cards():
    current_bunker = get_bunker()
    for i in range(players_count):
        file = open(f'/Users/manager/PycharmProjects/bunker/game/player_{i + 1}.txt', 'a')
        file.write(current_bunker['title'])
        file.write('\n')
        file.write(current_bunker['description'])
        file.write('\n\n')
        file.write(f'Состояние здоровья: {get_characteristic(health_list)} \n')
        file.close()


def save_remaining(abstract_list, type):
    file = open(f'/Users/manager/PycharmProjects/bunker/game/temp_{type}_remain.txt', 'w')
    for i in abstract_list:
        file.write(i)
    file.close()


create_cards()

save_remaining(health_list, 'health')
