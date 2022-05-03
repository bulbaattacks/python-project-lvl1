#!/usr/bin/env python3
import prompt
import random


rounds = 3
NAME = prompt.string('May I have your name? ')

def welcome_user():
    print('Welcome to the Brain Games!')
    print(f'Hello, {NAME}!')
    

def random_num_in_range(start, end):
    return random.randint(start, end)


def random_num():
    return random.randint(1, 6)


def ask(question):
    print(question)


def get_answer():
    return prompt.string('Your answer: ')


def succeed_game_over(NAME, counter):
    if counter == 3:
        print(f'Congratulations, {NAME}!')


def print_correct_answer():
    print('Correct!')


def print_wrong_answer(answer, right_answer, NAME):
    print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}")
    print(f"Let's try again, {NAME}!")
