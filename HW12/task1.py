# 1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
import json
import os.path

if os.path.exists('phone_book.json'):
    with open('phone_book.json', 'r') as file:
        phone_book = json.load(file)
else:
    phone_book = { "Adam" : 56474,
               "Andreo" : 45453,
               "Melisa" : 78475,}

print("Hello! I am a simple phone book. My commands:\nstats, add, delete, list, show")

while True:
    command = input("Enter command: ").lower()

    if command == "stats":
        print(f"I have {len(phone_book)} numbers")

    if command == "add":
        name_new_number = input("Name: ")
        if name_new_number in phone_book:
            print(f"You can't add {name_new_number}, it already exists")
            continue

        try:
            number = int(input("Number: "))
            phone_book[name_new_number] = number
            with open('phone_book.json', 'w') as file:
                json.dump(phone_book, file)
            print(f"{name_new_number} is added")
            print(f"Here is the updated phone book:\n {phone_book}")
        except ValueError:
            print('Please enter number')
            continue

    if command == "list":
        for phone_book_item in phone_book:
            print(phone_book_item)
        print(list(phone_book))

    if command == "delete":
        try:
            name_delete_number = input("Which number do you want to delete?: ")
            del phone_book[name_delete_number]
            with open('phone_book.json', 'w') as file:
                json.dump(phone_book, file)
            print(f"{name_delete_number} is deleted")
            print(f"Here is the updated phone book:\n {phone_book}")
        except KeyError:
            print('Please enter correct name')
            print(f"Here is the phone book:\n {phone_book}")
            continue

    if command == "show":
        number_info = input("Enter the name: ")
        try:
            print(f"{number_info}`s number: {phone_book[number_info]}")
        except KeyError:
            print('Please enter correct name')
            continue

    if command == "quit":
        print("Quit")
        break
