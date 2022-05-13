from random import randint
from math import sqrt

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_task_and_right_answer():
    task = randint(2, 100)
    right_answer = is_prime(task)
    return (task, right_answer)


def is_prime(num):
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return 'no'
    return 'yes'
