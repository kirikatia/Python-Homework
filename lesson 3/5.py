# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число: '))

positive = [0, 1]
for i in range(1, k):
    positive.append(positive[i] + positive[i-1])

negative = [0, 1]
for i in range(1, k):
    negative.append(negative[i-1] - negative[i])

new_list = []
for i in range(1, len(negative)+1):
    new_list.append(negative[-i])

new_list.extend(positive[1:])
print(new_list)