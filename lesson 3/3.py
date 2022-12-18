# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. 
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = input('Введите данные для списка(через пробел): ').split(' ')

maximum = 0
minimum = 1
for v in my_list:
    part = float(v) % 1
    if part > maximum:
        maximum = part
    if part < minimum and part > 0:
        minimum = part

print(round(maximum - minimum, 2))