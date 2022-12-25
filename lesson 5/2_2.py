# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

candies = int(input('Введите количество конфет: '))

order = random.randint(1, 2)

print(f'Первым ходит { "игрок" if order == 1 else "компьютер" }')

while candies > 28:
    if order == 1:
        k = int(input(f'Игрок, введите количество конфет: '))

        if k > 28 or k < 1:
            print('Нельзя взять больше 28 конфет или меньше 1')
            continue
    else:
        losing_state = int(candies / 29) * 29
        k = candies - losing_state
        k = random.randint(1, 28) if k <= 0 else k
        print(f'Компьютер берет {k} конфет')
        
    candies -= k
    order = 3 - order
    print(f'Осталось: {candies} конфет')

print(f'Победил { "игрок" if order == 1 else "компьютер" }')
