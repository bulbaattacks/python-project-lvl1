from random import randint, choice

RULE = 'What is the result of the expression?'


def run_round():
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

    return task, right_answer
