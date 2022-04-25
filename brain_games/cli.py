#!/usr/bin/env python3
import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def random_num():
    return random.randint(1, 100)


def random_operator():
    random_operators = ['-', '+', '*']
    return random.choice(random_operators)


def ask(question):
    print(question)


def get_answer():
    return prompt.string('Your answer: ')
