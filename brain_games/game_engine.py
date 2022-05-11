#!/usr/bin/env python3
from brain_games.cli import welcome_user, NAME
import prompt

ROUNDS = 3


def common_part(game):
    welcome_user()
    print(game.RULE)
    counter = 0

    for i in range(ROUNDS):
        task, right_answer = game.task_and_right_answer()
        print(f'Question: {task}')
        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            counter += 1
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(.', end=' ')
            print(f'Correct answer was {right_answer}')
            print(f"Let's try again, {NAME}!")
            break

    if counter == ROUNDS:
        print(f'Congratulations, {NAME}!')
