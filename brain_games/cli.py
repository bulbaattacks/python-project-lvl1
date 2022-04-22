#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even():
    counter = 0
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        num = randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')

        if (not even(num) and answer == 'no' or even(num) and answer == 'yes'):
            counter += 1
            print('Correct!')
        elif even(num) and answer != 'yes':
            print(f"{answer} is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        elif not even(num) and answer != 'no':
            print(f"{answer} is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break

    if counter == 3:
        print(f'Congratulations, {name}!')


def even(num):
    return num % 2 == 0
