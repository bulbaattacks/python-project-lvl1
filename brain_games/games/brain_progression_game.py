#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user, NAME, ROUNDS


def brain_progression():
    progression_question = 'What number is missing in the progression?'
    counter = 0
    welcome_user()
    print(progression_question)
    for i in range(ROUNDS):
        print('Question:', end=' ')
        right_answer = print_progression()
        print(' ')
        answer = prompt.string('Your answer: ')

        if int(answer) == right_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}")
            print(f"Let's try again, {NAME}!")
            break

    if counter == 3:
        print(f'Congratulations, {NAME}!')


def print_progression():
    start = randint(1, 10)
    step = randint(1, 10)
    end = start + (10 * step)
    blur_index = randint(1, 9)
    index = 0

    for i in range(start, end, step):
        if index == blur_index:
            right_answer = i
            print('..', end=' ')
        else:
            print(i, end=' ')
        index += 1

    return right_answer
