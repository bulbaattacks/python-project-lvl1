#!/usr/bin/env python3
from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
right_answer = 'yes'

def task_and_right_answer():
    num = randint(1, 100)
    right_answer = is_prime(num)
    task = f'Question: {num}'

    return (task, right_answer)


def is_prime(num):
    if num == 2 or num == 3:
        return 'yes'
    elif num % 2 == 0 or num == 1:
        return 'no'
    else:
        for i in range(3, num):
            if num % i == 0:
                return 'no'
            else:
                return 'yes'

