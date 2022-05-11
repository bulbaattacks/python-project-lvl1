from math import gcd
from random import randint

RULE = 'Find the greatest common divisor of given numbers.'


def task_and_right_answer():

    num1 = randint(1, 6)
    num2 = randint(1, 6)
    task = f'{num1} {num2}'
    right_answer = str(gcd(num1, num2))
    return (task, right_answer)
