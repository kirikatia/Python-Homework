# Создайте программу для игры в ""Крестики-нолики"".
import random

field = ['.' for x in range(0, 9)]

def show_field(field):
    print('Поле:')
    print(f'{field[0]} | {field[1]} | {field[2]}')
    print('----------')
    print(f'{field[3]} | {field[4]} | {field[5]}')
    print('----------')
    print(f'{field[6]} | {field[7]} | {field[8]}')

def check_win(field):
    for i in range(0, 3):
        if field[i*3] == field[i*3+1] == field[i*3+1] != '.':
            return field[i*3]

    for i in range(0, 3):
        if field[i] == field[i+3] == field[i+6] != '.':
            return field[i]

    for i in range(0, 2):
        if field[2*i] == field[4] == field[8-2*i] != '.':
            return field[2*i]

    return False
    
win = False
order = random.randint(1,2)

print(f'Первым ходит { "игрок (x)" if order == 1 else "компьютер (o)" }')

while not win:
    show_field(field)
    empty = [ind if val == '.' else -1 for ind, val in enumerate(field)]
    empty = [x for x in filter(lambda ind: ind >= 0, empty)]
    if len(empty) == 0:
        break

    if order == 1:
        coord = input('Введите координаты (x,y): ')
        (coord_x, coord_y) = coord.split(',')

        index = int(coord_x) + int(coord_y) * 3
        if index > 8:
            print('Введите корректные координаты')
            continue

        if field[index] != '.':
            print('Введите координаты незанятого места')
            continue
        field[index] = 'x'
    else:
        index = random.choice(empty)
        field[index] = 'o'
    
    order = 3 - order
    win = check_win(field)

show_field(field)
if win:
    print(f'Победили: {win}')
else:
    print(f'Ничья')