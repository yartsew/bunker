import random

players_count = int(input("Введите кол-во игроков: "))

health_list = list(open("/Users/manager/PycharmProjects/bunker/cards/health.txt"))

prepared_health_list = [i.strip("\n") for i in health_list]


def create_cards():
    for i in range(players_count):
        random_index = random.randint(0, len(health_list) - 1)
        file = open(f"/Users/manager/PycharmProjects/bunker/game/player_{i + 1}.txt", "a")
        file.write(f"Состояние здоровья: {prepared_health_list.pop(random_index)} \n")
        file.close()


create_cards()

