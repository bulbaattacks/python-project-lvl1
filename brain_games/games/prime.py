from random import randint
from math import sqrt

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_round():
    task = randint(1, 100)
    right_answer = 'yes' if is_prime(task) else 'no'
    return task, right_answer


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True
