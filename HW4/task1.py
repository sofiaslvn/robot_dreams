# 1. Створити програму, яка буде очікувати введення тексту від користувача і повідомляти — чи є
# введений текст “числом” чи “словом”.
# 2. Якщо введений текст “число”, програма має також вказати чи є воно парним чи непарним.
# 3. Якщо це “слово”, програма має вказати його довжину.

user_text = input('Please, type something: ')
if user_text.isdigit() == True:
    print("This is a number")
    if int(user_text) == 0:
        print("This chilo is not even or odd. It is zero.")
    elif int(user_text) % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")
else:
    print("This is a string")
    print(f"String length: {len(user_text)}")
