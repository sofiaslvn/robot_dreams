# Написати рекурсію, яка буде друкувати числа від введенного користувачем до нуля.
while True:
    def recursion(n):
        print(n, end=' ')
        if n == 0:
            return
        return recursion(n - 1)

    result = input('Enter number: ')
    print(recursion(int(result)))