"""Функция reduce"""
from functools import reduce

number = [1, 2, 3, 4, 5]


def sum_num(a, b):
    return a + b


print(f'Использование анонимной функции', reduce(lambda a, b: a + b, number))
print(f'Использование кастомной функции', reduce(sum_num, number))
