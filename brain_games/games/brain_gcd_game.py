#!/usr/bin/env python3
from math import gcd 
from brain_games.cli import welcome_user, random_num, ask, get_answer


def get_gcd():

    gcd_question = 'Find the greatest common divisor of given numbers.'
    counter = 0
    name = welcome_user()
    ask(gcd_question)

    for i in range(3):

        num1 = random_num()
        num2 = random_num()

        print(f'Question: {num1} {num2}')
        answer = get_answer()

        right_answer = gcd(num1, num2)

        if int(answer) == right_answer:
            counter += 1
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}")
            print(f"Let's try again, {name}!")
            break

    if counter == 3:
        print(f'Congratulations, {name}!')
