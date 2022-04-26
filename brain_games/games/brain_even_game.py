#!/usr/bin/env python3
from brain_games.cli import welcome_user, random_num, ask, get_answer, rounds, succeed_game_over, print_correct_answer, print_wrong_answer


def is_even():
    
    even_question = 'Answer "yes" if the number is even, otherwise answer "no".'
    yes_answer = 'yes'
    no_answer = 'no'
    counter = 0

    name = welcome_user()
    ask(even_question)

    for i in range(rounds):

        num = random_num()

        print(f'Question: {num}')
        answer = get_answer()

        if (even(num) and answer == yes_answer or not even(num) and answer == no_answer):
            counter += 1
            print_correct_answer()
        elif even(num) and answer != yes_answer:
            print_wrong_answer(answer, yes_answer, name)
            break
        elif not even(num) and answer != no_answer:
            print_wrong_answer(answer, no_answer, name)
            break

    succeed_game_over(name, counter)


def even(num):
    return num % 2 == 0
