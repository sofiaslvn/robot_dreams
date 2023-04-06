# Додати обробку помилок до коду з завдання №7 про телефонну книгу (тема: “Колекції та структури даних. Part 1”)
# Повинно бути як мінімум два блоки try except, де їх використовувати — вирішуєте самі.

print("Hello! I am a simple phone book. My commands:\nstats, add, delete, list, show")

phone_book = { "Adam" : 56474,
               "Andreo" : 45453,
               "Melisa" : 78475,
}
while True:
    command = input("Enter command: ").lower()

    if command == "stats":
        print(f"I have {len(phone_book)} numbers")

    if command == "add":
        name = input("Name: ")
        if name in phone_book:
            print(f"You can't add {name}, it already exists")
            continue
        try:
            number = input("Number: ")
            phone_book = {**phone_book, name: int(number)}
            print(f"{name} is added")
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
            print(f"{name_delete_number} is deleted")
            print(f"Here is the updated phone book:\n {phone_book}")
        except KeyError:
            print('Please enter correct name')
            print(f"Here is the phone book:\n {phone_book}")
            continue

    if command == "show":
        number_info = input("Enter the name: ")
        print(f"{number_info}`s number: {phone_book[number_info]}")

    if command == "quit":
        print("Quit")
        break