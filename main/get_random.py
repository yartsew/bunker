import random
import json

def get_characteristic(characteristic):
    random_index = random.randint(0, len(characteristic) - 1)
    return characteristic.pop(random_index)


def save_remaining(abstract_list, type):
    file = open(f'/Users/manager/PycharmProjects/bunker/game/system/temp_{type}_remain.txt', 'w')
    for i in abstract_list:
        file.write(f'{i}\n')
    file.close()


def prepare_list(abstract_list):
    prepared_list = [i.strip("\n") for i in abstract_list]
    return prepared_list

swapped_type = input('Укажите тип меняемой карты: baggage, bunker, facts, health, hobby, professions, specials, threats ')

if swapped_type in ['baggage', 'bunker', 'facts', 'health', 'hobby', 'professions']:
    swapped_list = list(open(f'/Users/manager/PycharmProjects/bunker/game/system/temp_{swapped_type}_remain.txt'))
    file = open(f'/Users/manager/PycharmProjects/bunker/game/new_{swapped_type}.txt', 'w')
    file.write(get_characteristic(swapped_list))
    file.close()
    save_remaining(prepare_list(swapped_list), f'{swapped_type}')
elif swapped_type in ['specials', 'threats']:
    with open(f'/Users/manager/PycharmProjects/bunker/game/system/temp_{swapped_type}_remain.json', 'r', encoding='utf-8') as f:
        swapped_list = json.load(f)
    new_swapped= dict(get_characteristic(swapped_list))
    file = open(f'/Users/manager/PycharmProjects/bunker/game/system/new_{swapped_type}.txt', 'w')
    file.write(f'{new_swapped["description"]}')
    file.close()
    with open(f'/Users/manager/PycharmProjects/bunker/game/system/temp_{swapped_type}_remain.json', 'w') as f:
        json.dump(swapped_list, f, ensure_ascii=False)
else:
    print("Invadid type")

