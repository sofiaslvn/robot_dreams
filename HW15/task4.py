# Створити клас User, який в конструкторі має приймати параметр name і ініціалізувати його у відповідний атрибут.
# Перевизначити метод eq таким чином, щоб при порівнянні 2 обʼєктів типу User у який співпадають атрибути name,
# ми отримали True. При цьому не враховувати регістр, в якому записані кожен із атрибутів.

class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name.lower() == other.name.lower()
        else:
            return True

first_user = User('OLEKSII')
second_user = User('Oleksii')
print(first_user == second_user)