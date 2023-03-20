# 1. Створити програму, яка буде очікувати від користувача введення тексту і виведе інформацію
# по кожному надрукованому символу:
# це “число” + яке воно (парне, непарне),
# це “буква” + яка вона (велика чи маленька),
# це “символ”

user_text = input("Please, type something: ")
info = list(user_text)
print(info)
for symbol in info:
    print(symbol)
    if symbol.isdigit() == True:
        print(f"This is a number {symbol}")
        if int(symbol) == 0:
            print("This number is not even or odd. It is zero.")
        elif int(symbol) % 2 == 0:
            print("This is an even number")
        else:
            print("This is an odd number")
    elif symbol.isalpha() == True:
        print(f"This is a letter {symbol}")
        if symbol.isupper() == True:
            print(f"{symbol} is upper case")
        else:
            print(f"{symbol} is lower case")
    else:
        print(f"This is a '{symbol}' symbol")