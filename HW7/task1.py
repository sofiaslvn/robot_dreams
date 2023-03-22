# 1. Створити телефонну книгу, яка матиме наступні команди:
# stats: кількість записів; add: додати запис; delete <name>: видалити запис за іменем (ключем)
# list: список всіх імен в книзі; show <name>: детальна інформація по імені

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
        number = input("Number: ")
        phone_book = {**phone_book, name: int(number)}
        print(f"{name} is added")
        print(f"Here is the updated phone book:\n {phone_book}")

    if command == "list":
        for l in phone_book:
            print(l)
        print(list(phone_book))

    if command == "delete":
        name_delete_number = input("Which number do you want to delete?: ")
        del phone_book[f'{name_delete_number}']
        print(f"{name_delete_number} is deleted")
        print(f"Here is the updated phone book:\n {phone_book}")

    if command == "show":
        number_info = input("Enter the name: ")
        print(f"{number_info}`s number: {phone_book[number_info]}")

    if command == "quit":
        print("Quit")
        break