#Задайте список из n чисел последовательности (1 + 1/n)^n. 
#Вывести в консоль сам список и сумму его элементов.

number = int(input('Введите число: '))
if number == 0:
    print('Введите число больше 0')
else:
    new_list = []
    for x in range(1, number+1):
        new_list.append(round((1+1/x)**x, 2))
    print (new_list, end = ',')
    print('\n')
    print(sum(new_list))