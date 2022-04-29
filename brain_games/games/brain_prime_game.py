#!/usr/bin/env python3
from brain_games.cli import (welcome_user, ask, get_answer, rounds,
                             succeed_game_over, print_correct_answer,
                             print_wrong_answer, random_num_in_range)


def is_prime():

    prime_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    counter = 0
    name = welcome_user()
    ask(prime_question)

    for i in range(rounds):
        num = random_num_in_range(1, 100)

        print(f'Question: {num}')
        answer = get_answer()
        right_answer = 'yes'

        for i in range(2, num):
            if num <= 3:
                break
            elif num % i == 0:
                right_answer = 'no'
                break

        if answer == right_answer:
            print_correct_answer()
            counter += 1
        else:
            print_wrong_answer(answer, right_answer, name)
            break

    succeed_game_over(name, counter)