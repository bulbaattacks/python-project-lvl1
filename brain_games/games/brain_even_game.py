#!/usr/bin/env python3
from brain_games.cli import welcome_user, random_num, ask, get_answer


def is_even():
    even_question = 'Answer "yes" if the number is even, otherwise answer "no".'
    counter = 0
    name = welcome_user()
    ask(even_question)

    for i in range(3):
        num = random_num()
        print(f'Question: {num}')
        answer = get_answer()

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
