# Створити функцію, яка сумує будь-яку кількість аргументів і повертає результат.
def sum(*args):
    sum_of_numbers = 0

    for number in args:
        sum_of_numbers = sum_of_numbers + number
    print(sum_of_numbers)


sum(4, 6, 7)
sum(4, 6, 109, -200)
