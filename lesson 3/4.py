# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

x = int(input('Введите число: '))

my_list = []
while x > 0:
    my_list.append(x % 2)
    x = int(x / 2)

my_number = ''
for i in range(1, len(my_list)+1):
    my_number += str(my_list[-i])
    
print(my_number)