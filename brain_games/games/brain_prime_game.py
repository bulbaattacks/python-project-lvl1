#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user, NAME, ROUNDS


def is_prime():

    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    counter = 0
    welcome_user()
    print(question)

    for i in range(ROUNDS):
        num = randint(1, 100)

        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        right_answer = 'yes'

        for i in range(1, num):
            if num <= 3:
                break
            elif num % i == 0 or i == 1:
                right_answer = 'no'
                break

        if answer == right_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}")
            print(f"Let's try again, {NAME}!")
            break

    if counter == 3:
        print(f'Congratulations, {NAME}!')
