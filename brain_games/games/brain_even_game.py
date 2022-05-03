#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user, NAME, ROUNDS


def is_even():

    even_question = 'Answer "yes" if the number is even, otherwise answer "no".'
    yes_answer = 'yes'
    no_answer = 'no'
    counter = 0

    welcome_user()
    print(even_question)

    for i in range(ROUNDS):

        num = randint(1, 6)

        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')

        if even(num):
            if answer == yes_answer:
                counter += 1
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was {yes_answer}")
                print(f"Let's try again, {NAME}!")
                break

        if not even(num):
            if answer == no_answer:
                counter += 1
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was {no_answer}")
                print(f"Let's try again, {NAME}!")
                break

    if counter == 3:
        print(f'Congratulations, {NAME}!')


def even(num):
    return num % 2 == 0
