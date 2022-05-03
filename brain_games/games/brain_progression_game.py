#!/usr/bin/env python3
from brain_games.cli import (welcome_user, NAME, ask, get_answer, rounds,
                             succeed_game_over, random_num_in_range,
                             print_correct_answer, print_wrong_answer)


def brain_progression():
    progression_question = 'What number is missing in the progression?'
    counter = 0
    welcome_user()
    ask(progression_question)
    for i in range(rounds):
        print('Question:', end=' ')
        right_answer = print_progression()
        print(' ')
        answer = get_answer()

        if int(answer) == right_answer:
            print_correct_answer()
            counter += 1
        else:
            print_wrong_answer(answer, right_answer, NAME)
            break

    succeed_game_over(NAME, counter)


def print_progression():
    start = random_num_in_range(1, 10)
    step = random_num_in_range(1, 10)
    end = start + (10 * step)
    blur_index = random_num_in_range(0, 9)
    index = 0

    for i in range(start, end, step):
        if index == blur_index:
            right_answer = i
            print('..', end=' ')
        else:
            print(i, end=' ')
        index += 1

    return right_answer
