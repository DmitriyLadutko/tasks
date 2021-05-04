"""Функция reduce"""
from functools import reduce

number = [1, 2, 3, 4, 5]


def sum_num(a, b):
    return a + b


print(f'Использование анонимной функции', reduce(lambda a, b: a + b, number))
print(f'Использование кастомной функции', reduce(sum_num, number))

print('-------------------------------------------------------------------------------')


def hello(name: str) -> str:
    return f'Hello {name}'


def good_bye(name: str) -> str:
    return f'Good bye {name}'


def some_fun(func):
    return func("Dima")


print(some_fun(hello))
print('-------------------------------------------------------------------------------')


def parent_fun():
    print('parent print')

    """Определение функции не говорит о порядке ее вызова"""

    def second_child():
        print('second print')

    def first_child():
        print('first print')

    """Порядок вызова определяется здесь"""
    first_child()
    second_child()


parent_fun()

"""Декоратор"""


def some_decorator(func):
    def wrapper():
        print(f'Before call function')
        func()
        print(f'After call function')

    return wrapper


@some_decorator
def call_fun():
    print('Call func')


call_fun()