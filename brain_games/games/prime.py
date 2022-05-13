from random import randint
from math import sqrt

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_task_and_right_answer():
    num = randint(2, 100)
    right_answer = is_prime(num)
    task = num
    return (task, right_answer)


def is_prime(num):
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return 'no'
    return 'yes'
