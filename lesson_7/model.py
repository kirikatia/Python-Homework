first_number = 0
intermediate_result = 0
next_number = 0

def summa() -> float:
    global intermediate_result
    global next_number
    global first_number
    intermediate_result = first_number + next_number
    first_number = intermediate_result


def difference() -> float:
    global intermediate_result
    global next_number
    global first_number
    intermediate_result = first_number - next_number
    first_number = intermediate_result


def multiplication() -> float:
    global intermediate_result
    global next_number
    global first_number
    intermediate_result = first_number * next_number
    first_number = intermediate_result


def division() -> float:
    global intermediate_result
    global next_number
    global first_number
    intermediate_result = first_number / next_number
    first_number = intermediate_result


def check_operation(sm_operation: str):
    if sm_operation == '+':
        summa()
    elif sm_operation == '-':
        difference()
    elif sm_operation == '*':
        multiplication()
    elif sm_operation == '/':
        division()

def get_intermediate_result() -> float:
    global intermediate_result
    return intermediate_result

def set_intermediate_result(smth):
    global intermediate_result
    intermediate_result = smth

def set_next_number(smth):
    global next_number
    next_number = smth

def get_next_number() -> float:
    global next_number
    return next_number

def set_first_number(smth):
    global first_number
    global intermediate_result
    first_number = smth
    intermediate_result = first_number