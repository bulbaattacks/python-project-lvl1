from random import randint

RULE = 'What number is missing in the progression?'


def get_task_and_right_answer():
    mass_num = []
    num = randint(5, 10)
    start = randint(1, 10)
    step = randint(1, 10)
    end = start + (step * num)
    mass_num = list(range(start, end, step))
    mass_num = [str(i) for i in mass_num]

    blur_index = randint(0, len(mass_num) - 1)
    blur_num = '..'
    right_answer = mass_num[blur_index]
    mass_num[blur_index] = blur_num
    task = ' '.join(mass_num)
    return task, right_answer
