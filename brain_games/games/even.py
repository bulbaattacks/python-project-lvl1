from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_task_and_right_answer():

    num = randint(1, 6)
    right_answer = 'yes' if num % 2 == 0 else 'no'
    task = num
    return (task, right_answer)
