# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Первым ходом нужно взять 20 конфет

import random

candies = int(input('Введите количество конфет: '))

order = random.randint(1, 2)

print(f'Первым ходит игрок {order}')

while candies > 28:
    k = int(input(f'Игрок {order}, введите количество конфет: '))
    if k > 28 or k < 1:
        print('Нельзя взять больше 28 конфет или меньше 1')
        continue

    candies -= k
    order = 3 - order
    print(f'Осталось: {candies} конфет')

print(f'Победил игрок {order}')