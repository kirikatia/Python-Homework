# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
string = input('Введите строку: ')

words = string.split(' ')

result_words = filter(lambda x: 'абв' not in x, words)

result_string = ' '.join(result_words)

print(result_string)