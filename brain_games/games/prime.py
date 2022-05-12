from random import randint
import sympy

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def task_and_right_answer():
    num = randint(1, 100)
    right_answer = 'yes' if sympy.isprime(num) == True else 'no'
    task = num
    return (task, right_answer)
