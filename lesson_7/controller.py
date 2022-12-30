import model
import view
import logger

def start():
    logger.log_message('Calculator Start')
    expression = view.first_input()

    if isfloat(expression):
        logger.log_message('Button Mode')
        button_mode(float(expression))
    else:
        logger.log_message('String Mode')
        string_mode(expression)
    
    logger.log_message('Calculator Stop')

def input_and_check_operation():
    while True:
        operation = view.input_operation()
        if operation in ['+', '-', '/', '*', '=']:
            return operation
        view.print_error()

def input_and_check_number():
    while True:
        expression = view.input_number()
        if isfloat(expression):
            return float(expression)
        view.print_error()

def button_mode(first_number):
    model.set_first_number(first_number)
    operation = input_and_check_operation()

    while operation != '=':
        first = model.get_intermediate_result()

        second = input_and_check_number()
        model.set_next_number(second)
        model.check_operation(operation)

        res = model.get_intermediate_result()
        view.print_result(model.get_intermediate_result())
        logger.log_operation(first, second, operation, res)

        operation = input_and_check_operation()

    view.print_result(model.get_intermediate_result())

def string_mode(expression):
    res = eval(expression)
    logger.log_expression(expression, res)
    view.print_result(res)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
