# 1. Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
# Декоратор має працювати для різних функцій однаково.
import datetime
def my_decorator(func):
    def wraper(*args, **kwargs):
        func(*args, **kwargs)
        print(f'My name is {func.__name__}')
        time = datetime.datetime.now()
        print(f'Time {time}')
    return wraper


@my_decorator
def my_func():
    print("Hello. I am a function")


@my_decorator
def my_second_func(a, b):
    print("Hello. I am a second function")
    print(f'My result is {a + b}')


my_func()
my_second_func(11, 45)