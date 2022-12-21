# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
filename1 = input('Введите название первого файла: ')
filename2 = input('Введите название второго файла: ')

def read_polynomial(filename):
    superscript_map = { "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹" }
    power_map = {v: k for k, v in superscript_map.items()}

    with open(filename, 'r', encoding='UTF-8') as file:
        polynomial_string = file.read()

    polynomial = {}
    parts = polynomial_string.split('=')[0].split(' + ')
    for part in parts:
        if '*' in part:
            [coeff, x] = part.split(' * ')
            power = ''
            for symbol in x:
                if symbol in power_map:
                    power += power_map[symbol]

            if power == '':
                power = '1'
        else:
            coeff = part
            power = '0'

        polynomial[int(power)] = int(coeff)
        
    return polynomial

# Функция для форматирования степени
def format_power(power):
    superscript_map = { "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹" }
    result = ''
    for symbol in str(power):
        result += superscript_map[symbol]
    return result

polynomial1 = read_polynomial(filename1)
polynomial2 = read_polynomial(filename2)

max_power = max([*polynomial1.keys(), *polynomial2.keys()])

polynomial = ''
for i in range(max_power, -1, -1):
    coeff = 0
    if i in polynomial1:
        coeff += polynomial1[i]
    if i in polynomial2:
        coeff += polynomial2[i]

    if coeff == 0:
        continue

    if polynomial != '':
        polynomial += ' + '

    polynomial += f'{coeff}'

    if i > 1:
        polynomial += f' * x{format_power(i)}'
    elif i == 1:
        polynomial += f' * x'

polynomial += ' = 0'
print(polynomial)