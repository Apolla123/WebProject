import random


def get_number(n1, n2):
    # Получить случайное число от 0 до заданного числа
    random_number = random.randint(n1, n2)

    # Вывести случайное число
    return int(random_number)