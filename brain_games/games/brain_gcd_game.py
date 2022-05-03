#!/usr/bin/env python3
import prompt
from math import gcd
from random import randint
from brain_games.cli import welcome_user, NAME, ROUNDS


def get_gcd():

    gcd_question = 'Find the greatest common divisor of given numbers.'
    counter = 0
    welcome_user()
    print(gcd_question)

    for i in range(ROUNDS):

        num1 = randint(1, 6)
        num2 = randint(1, 6)

        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ')

        right_answer = gcd(num1, num2)

        if int(answer) == right_answer:
            counter += 1
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}")
            print(f"Let's try again, {NAME}!")
            break

    if counter == 3:
        print(f'Congratulations, {NAME}!')
