
def input_number():
    number = input('Введите число: ')
    return number

def input_operation():
    operation = input('Введите операцию (+, -, *, /, =): ')
    return operation

def first_input():
    return input('Введите число или выражение: ')

def print_result(smth):
    print(f'Результат: {smth}')

def print_error():
    print(f'Ошибка, некорректный ввод!')