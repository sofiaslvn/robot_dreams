# 2. Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює
# перед виконанням коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює. У випадку
# виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити своєї роботи.
class TenEqualSigns:
    def __enter__(self):
        print(10*'=')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(10 * '=')
        if exc_type:
            print(f"Error occurred")
            return True

with TenEqualSigns():
    print('Hello')
    print(1/0)