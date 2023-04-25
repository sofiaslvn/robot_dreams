# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.
import datetime
def my_decorator(func):
    def wraper(*args, **kwargs):
        func(*args, **kwargs)
        print(f'My name is {func.__name__}')
        time = datetime.datetime.now()
        print(f'Time {time}')
        with open('nametime.txt', 'a') as f:
            f.write(f'{func.__name__} called at {datetime.datetime.now()}\n')
    return wraper


@my_decorator
def my_func():
    print("Hello. I am a function")
my_func()


@my_decorator
def my_second_func(a, b):
    print("Hello. I am a second function")
    print(f'My result is {a + b}')
my_second_func(11, 45)