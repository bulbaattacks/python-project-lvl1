#!/usr/bin/env python3
import random
from brain_games.cli import (welcome_user, random_num, ask, get_answer, rounds,
                             succeed_game_over, print_correct_answer,
                             print_wrong_answer)


def calc_game():

    calc_question = 'What is the result of the expression?'
    counter = 0

    name = welcome_user()
    ask(calc_question)

    for i in range(rounds):

        num1 = random_num()
        num2 = random_num()
        operator = random_operator()

        print(f'Question: {num1} {operator} {num2}')
        answer = get_answer()

        right_answer = eval(f'{num1} {operator} {num2}')

        if int(answer) == right_answer:
            counter += 1
            print_correct_answer()
        else:
            print_wrong_answer(answer, right_answer, name)
            break

    succeed_game_over(name, counter)


def random_operator():
    random_operators = ['-', '+', '*']
    return random.choice(random_operators)
