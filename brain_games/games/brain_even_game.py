#!/usr/bin/env python3
from brain_games.cli import (welcome_user, NAME, random_num, ask, get_answer, rounds,
                             succeed_game_over, print_correct_answer,
                             print_wrong_answer, name)


def is_even():

    even_question = 'Answer "yes" if the number is even, otherwise answer "no".'
    yes_answer = 'yes'
    no_answer = 'no'
    counter = 0

    welcome_user()
    ask(even_question)

    for i in range(rounds):

        num = random_num()

        print(f'Question: {num}')
        answer = get_answer()

        if even(num):
            if answer == yes_answer:
                counter += 1
                print_correct_answer()
            else:
                print_wrong_answer(answer, yes_answer, NAME)
                break

        if not even(num):
            if answer == no_answer:
                counter += 1
                print_correct_answer()
            else:
                print_wrong_answer(answer, no_answer, NAME)
                break

    succeed_game_over(NAME, counter)


def even(num):
    return num % 2 == 0
