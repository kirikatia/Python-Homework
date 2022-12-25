# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

mode = int(input('Введите режим (0 - сжатие, 1 - восстановление): '))
if mode < 0 or mode > 1:
    print('Неправильный режим')
    exit(0)

file_src = input('Введите название исходного файла: ')
file_dst = input('Введите название целевого файла: ')

if mode == 0:
    with open(file_src, 'r') as file:
        data = file.read()
    
    result = ''
    count = 1
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            count += 1
        else:
            result += f'{count}{data[i]}'
            count = 1

    if count > 1 or (len(data) > 2 and data[-2] != data[-1]):
        result += f'{count}{data[-1]}'

    with open(file_dst, 'w') as file:
        file.write(result)
else:
    with open(file_src, 'r') as file:
        data = file.read()
    
    result = ''
    number = ''
    for symbol in data:
        if symbol.isnumeric():
            number += symbol
        else:
            result += int(number) * symbol
            number = ''
    
    with open(file_dst, 'w') as file:
        file.write(result)