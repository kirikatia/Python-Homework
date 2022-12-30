from datetime import datetime as dt

path = 'log.txt'

def log_operation(first, second, oper, res):
    log_expression(f'{first} {oper} {second}', res)

def log_expression(expression, res):
    log_message(f'{expression} = {res}')

def log_message(message):
    with open(path, 'a') as data:
        data.write(f'{dt.now()} | {message}\n')