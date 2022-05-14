from random import randint

RULE = 'What number is missing in the progression?'


def run_round():
    generate_progression = []
    num = randint(5, 10)
    start = randint(1, 10)
    step = randint(1, 10)
    end = start + (step * num)
    generate_progression = list(range(start, end, step))
    progression = [str(i) for i in generate_progression]

    random_index = randint(0, len(progression) - 1)
    right_answer, progression[random_index] = progression[random_index], '..'
    task = ' '.join(progression)
    return task, right_answer
