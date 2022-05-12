from random import randint
import sympy

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def task_and_right_answer():
    task = randint(1, 100)
    right_answer = 'yes' if sympy.isprime(task) else 'no'
    return (task, right_answer)
