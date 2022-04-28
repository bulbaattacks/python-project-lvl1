#!/usr/bin/env python3
import prompt
import random


rounds = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def random_num_in_range(start, end):
    return random.randint(start, end)


def random_num():
    return random.randint(1, 6)


def ask(question):
    print(question)


def get_answer():
    return prompt.string('Your answer: ')


def succeed_game_over(name, counter):
    if counter == 3:
        print(f'Congratulations, {name}!')


def print_correct_answer():
    print('Correct!')


def print_wrong_answer(answer, right_answer, name):
    print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}")
    print(f"Let's try again, {name}!")
