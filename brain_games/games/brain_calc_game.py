#!/usr/bin/env python3
import prompt
from random import randint, choice
from brain_games.cli import welcome_user, NAME, ROUNDS


def calc_game():

    calc_question = 'What is the result of the expression?'
    counter = 0

    welcome_user()
    print(calc_question)

    for i in range(ROUNDS):

        num1 = randint(1, 6)
        num2 = randint(1, 6)
        operator = random_operator()

        print(f'Question: {num1} {operator} {num2}')
        answer = prompt.string('Your answer: ')

        right_answer = eval(f'{num1} {operator} {num2}')

        if int(answer) == right_answer:
            counter += 1
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}")
            print(f"Let's try again, {NAME}!")
            break

    if counter == 3:
        print(f'Congratulations, {NAME}!')


def random_operator():
    random_operators = ['-', '+', '*']
    return choice(random_operators)
