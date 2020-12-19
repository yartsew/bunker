import random

shuffle = []

while True:
    new_input = input('Введите значения через Enter, для выхода - q ')
    if new_input != 'q':
        shuffle.append(new_input)
    else:
        break
random.shuffle(shuffle)
file = open(f'/Users/manager/PycharmProjects/bunker/game/shuffle.txt', 'w')
for i in shuffle:
    file.write(f'{i}\n')
