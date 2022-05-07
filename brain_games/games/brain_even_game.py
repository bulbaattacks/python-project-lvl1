#!/usr/bin/env python3
from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'

def task_and_right_answer():
    
    yes_answer = 'yes'
    no_answer = 'no'
    num = randint(1, 6)
    right_answer = is_even(num)
    task = f'Question: {num}'
    
    return (task, right_answer)


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'
