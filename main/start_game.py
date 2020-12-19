import random
import json

players_count = int(input('Введите кол-во игроков: '))

health_list = list(open('/Users/manager/PycharmProjects/bunker/cards/health.txt'))
baggage_list = list(open('/Users/manager/PycharmProjects/bunker/cards/baggage.txt'))
facts_list = list(open('/Users/manager/PycharmProjects/bunker/cards/facts.txt'))
hobby_list = list(open('/Users/manager/PycharmProjects/bunker/cards/hobby.txt'))
professions_list = list(open('/Users/manager/PycharmProjects/bunker/cards/professions.txt'))
with open('/Users/manager/PycharmProjects/bunker/cards/specials.json', 'r', encoding='utf-8') as f:
    specials_list = json.load(f)
bunker_list = list(open('/Users/manager/PycharmProjects/bunker/cards/bunker.txt'))
with open('/Users/manager/PycharmProjects/bunker/cards/threats.json', 'r', encoding='utf-8') as f:
    threads_list = json.load(f)


def prepare_list(abstract_list):
    prepared_list = [i.strip("\n") for i in abstract_list]
    return prepared_list


def get_accident():
    with open('/Users/manager/PycharmProjects/bunker/cards/accident.json', 'r', encoding='utf-8') as f:
        accident_list = json.load(f)
    return random.choice(accident_list)


def get_characteristic(characteristic):
    random_index = random.randint(0, len(characteristic) - 1)
    return characteristic.pop(random_index)

def random_serious():
    return random.choice(['Ремиссия', 'В легкой форме', 'В средней форме', 'В тяжелой форме'])

def random_bio ():
    age = random.randint(18, 65)
    gender = random.choice(['мужчина', 'женщина'])
    orientation = random.choice(['Гетеро', 'Гомо', 'Би'])
    return f'{gender} {age} лет - {orientation}\n'

def create_cards():
    current_bunker = get_accident()
    for i in range(players_count):
        prepared_health = get_characteristic(health_list).strip("\n")
        user_special = get_characteristic(specials_list)
        file = open(f'/Users/manager/PycharmProjects/bunker/game/player_{i + 1}.txt', 'a')
        file.write(f'{current_bunker["title"]}\n{current_bunker["description"]}\n\n')
        file.write(random_bio())
        file.write(f'Состояние здоровья: {prepared_health} {random_serious()}\n')
        file.write(f'Хобби: {get_characteristic(hobby_list)}')
        file.write(f'Багаж: {get_characteristic(baggage_list)}')
        file.write(f'Случайный факт: {get_characteristic(facts_list)}')
        file.write(f'Специальная карта:\n{user_special["title"]}: {user_special["description"]}')
        file.close()


def save_remaining(abstract_list, type):
    file = open(f'/Users/manager/PycharmProjects/bunker/game/system/temp_{type}_remain.txt', 'w')
    for i in abstract_list:
        file.write(f'{i}\n')
    file.close()


create_cards()

save_remaining(prepare_list(health_list), 'health')
save_remaining(prepare_list(baggage_list), 'baggage')
save_remaining(prepare_list(facts_list), 'facts')
save_remaining(prepare_list(hobby_list), 'hobby')
save_remaining(prepare_list(professions_list), 'professions')
with open('/Users/manager/PycharmProjects/bunker/game/system/temp_specials_remain.json', 'w') as f:
    json.dump(specials_list, f, ensure_ascii=False)
save_remaining(prepare_list(bunker_list), 'bunker')
with open('/Users/manager/PycharmProjects/bunker/game/system/temp_threats_remain.json', 'w') as f:
    json.dump(threads_list, f, ensure_ascii=False)
