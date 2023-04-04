# Написати програму, яка буде повертати факторіал введеного числа, використовуючи рекурсію.
while True:
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    result = input('Enter number: ')
    print(factorial(int(result)))