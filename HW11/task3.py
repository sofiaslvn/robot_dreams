# 3. Переписати декоратор із першого завдання, щоб він приймав цілочисельний аргумент `times`.
# Стільки разів виконувавати друк назви функції і часу, скільки ‘times’ задано.
import datetime

def my_decorator(times=1):
    def timedecorator(func):
        def wraper(*args, **kwargs):
            func(*args, **kwargs)
            print(f'\nMy name is {func.__name__}'*times)
            time = datetime.datetime.now()
            print(f'\nTime {time}'*times)
        return wraper
    return timedecorator


@my_decorator(times=2)
def my_func():
    print("Hello. I am a function")


@my_decorator(times=2)
def my_second_func(a, b):
    print("Hello. I am a second function")
    print(f'My result is {a + b}')


my_func()
my_second_func(11, 45)