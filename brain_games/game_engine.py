#!/usr/bin/env python3
import prompt

ROUND = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)

    for i in range(ROUND):
        task, right_answer = game.get_task_and_right_answer()
        print(f'Question: {task}')
        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(.', end=' ')
            print(f'Correct answer was {right_answer}')
            print(f"Let's try again, {name}!")
            break

    else:
        print(f'Congratulations, {name}!')
