# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите степень многочлена: '))
filename = input('Введите название файла: ')

# Функция для форматирования степени
def format_power(power):
    superscript_map = { "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹" }
    result = ''
    for symbol in str(power):
        result += superscript_map[symbol]
    return result

# Многочлен
polynomial = ''

# Генерируем коэффициенты начиная со старшей степени
for i in range(k, -1, -1):
    # Для самой старшей степени коэффициент должен быть > 0
    coeff = random.randint(0 if i < k else 1, 100)

    # Если коэффициент 0, то пропускаем член
    if coeff == 0:
        continue

    if i < k:
        polynomial += ' + '

    polynomial += f'{coeff}'

    if i > 1:
        polynomial += f' * x{format_power(i)}'
    elif i == 1:
        polynomial += f' * x'

polynomial += ' = 0'
# Выводим результат на экран
print(polynomial)

# Пишем результат в файл
with open(filename, 'w', encoding='UTF-8') as file:
    file.write(polynomial)
