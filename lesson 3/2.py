# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

my_list = input('Введите данные для списка(через пробел): ').split(' ')

new_list = []

half = len(my_list) / 2
if half % 1 > 0:
    half = int(half) + 1
else:
    half = int(half)

for i in range(half):
    new_list.append(int(my_list[i]) * int(my_list[-(i+1)]))

print(new_list)
