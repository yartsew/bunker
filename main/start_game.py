import random

players_count = int(input("Введите кол-во игроков: "))

health_list = list(open("/Users/manager/PycharmProjects/bunker/cards/health.txt"))


def prepare_list(abstract_list):
    i = 0
    for element in abstract_list:
        abstract_list[i] = element.strip("\n")
        i = i + 1
    return


def create_cards():
    for i in range(players_count):
        random_index = random.randint(0, len(health_list) - 1)
        file = open(f"/Users/manager/PycharmProjects/bunker/game/player_{i + 1}.txt", "a")
        file.write(f"Состояние здоровья: {health_list.pop(random_index)} \n")
        file.close()


prepare_list(health_list)
create_cards()

