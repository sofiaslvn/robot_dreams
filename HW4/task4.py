# 4. Створити програму, яка буде очікувати введення тексту від користувача і повідомляти якого типу введені дані.
# Використати match, case і вбудовані функції Python

text = True

match text:
    case str():
        print("text type")
    case bool():
        print("boolean type")
    case int():
        print("numeric type")

# Не змогла розібратись як зробити це через input :(