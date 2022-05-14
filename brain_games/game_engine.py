import prompt

ROUNDS_COUNT = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)

    for i in range(ROUNDS_COUNT):
        task, right_answer = game.run_round()
        print(f'Question: {task}')
        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(.', end=' ')
            print(f'Correct answer was {right_answer}')
            print(f"Let's try again, {name}!")
            break

    else:
        print(f'Congratulations, {name}!')
