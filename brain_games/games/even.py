from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_round():
    task = randint(1, 6)
    right_answer = 'yes' if task % 2 == 0 else 'no'
    return task, right_answer
