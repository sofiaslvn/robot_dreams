# Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occurred".
print("Hello! I am a simple phone book. My commands:\nstats, add, delete, list, show")

class MyCustomException(Exception):
    pass

    def get_error_code(self):
        return self.error_code

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
            if number.isdigit() == False:
                raise MyCustomException
            else:
                phone_book = {**phone_book, name: int(number)}
                print(f"{name} is added")
                print(f"Here is the updated phone book:\n {phone_book}")
        except MyCustomException:
            print(f"Custom exception is occurred")

    if command == "list":
        for phone_book_item in phone_book:
            print(phone_book_item)
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