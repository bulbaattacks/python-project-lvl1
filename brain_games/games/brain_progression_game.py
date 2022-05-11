from random import randint

RULE = 'What number is missing in the progression?'


def task_and_right_answer():
    start = randint(1, 10)
    step = randint(1, 10)
    end = start + (10 * step)
    blur_index = randint(1, 9)
    index = 0
    task = ' '

    for i in range(start, end, step):
        if index == blur_index:
            right_answer = str(i)
            task += ".. "
        else:
            task += f'{i} '
        index += 1
    return task, right_answer
