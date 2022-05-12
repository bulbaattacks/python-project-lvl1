from random import randint
import sympy

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def task_and_right_answer():
    num = randint(1, 100)
    right_answer = is_prime(num)
    task = f'Question: {num}'
    return (task, right_answer)


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return 'no'
    return 'yes'
