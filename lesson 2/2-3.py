#Реализуйте алгоритм перемешивания списка.
#Встроенный алгоритм SHUFFLE не использовать! 
#Реализовать свой метод
import random

my_list = input('Введите данные для списка(через пробел): ').split(' ')
print()

ln = len(my_list)

for i in range(ln):
    x = random.randint(0, ln-1)
    my_list.append(my_list.pop(x))

print(my_list)