# Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі,
# використовуючи рекурсію.
while True:
    def fibonacci(n):
        if n in [0, 1]:
            return n
        return fibonacci(n-1)+fibonacci(n-2)

    result = input('Enter number: ')
    print(fibonacci(int(result)))