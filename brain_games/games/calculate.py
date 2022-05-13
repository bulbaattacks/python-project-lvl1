from random import randint, choice

RULE = 'What is the result of the expression?'


def get_task_and_right_answer():

    num1 = randint(1, 6)
    num2 = randint(1, 6)
    random_operators = ['-', '+', '*']
    operator = choice(random_operators)
    task = f'{num1} {operator} {num2}'
    if operator == '-':
        right_answer = str(num1 - num2)
    elif operator == '+':
        right_answer = str(num1 + num2)
    elif operator == '*':
        right_answer = str(num1 * num2)

    return (task, right_answer)
