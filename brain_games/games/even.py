from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def task_and_right_answer():

    num = randint(1, 6)
    right_answer = is_even(num)
    task = num
    return (task, right_answer)


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'
