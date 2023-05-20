# Створити клас MyStr(str), який має перевизначтити метод str таким чином,
# щоб замість друку реального значення всі літери були переведені в верхній регістр

class MyStr(str):
    def __init__(self, string):
        self.string=string

    def __str__(self):
        return self.string.upper()

my_str = MyStr('test')
print(my_str)