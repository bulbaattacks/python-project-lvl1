from random import randint, choice

RULE = 'What is the result of the expression?'


def task_and_right_answer():

    num1 = randint(1, 6)
    num2 = randint(1, 6)
    operator = random_operator()
    task = f'Question: {num1} {operator} {num2}'
    right_answer = str(eval(f'{num1} {operator} {num2}'))
    return (task, right_answer)


def random_operator():
    random_operators = ['-', '+', '*']
    return choice(random_operators)
