
import os.path
import json
import re
import telebot
import random


bot = telebot.TeleBot('5929515446:AAH2IlbnOqHKOqWVleAqGmJ7HKps1XOETdw')

def validate_phone_number(phone_number):
    return bool(re.match(r"(\+?3?8?)?0?\d{9}$", phone_number))

if os.path.exists('phone_book.json'):
    with open('phone_book.json', 'r') as file:
        phone_book = json.load(file)
else:
    phone_book = { "Adam" : "+380768594758",
                   "Andreo" : "380768594758",
                   "Melisa" : "0768594758"}

@bot.message_handler(commands=['start',])
def hello(message):
    bot.send_message(message.chat.id, 'Hello! I am a Pawsome pics bot. I have a function to send cute pictures '
                                      'and a phone book. \nMy /commands')

@bot.message_handler(commands=['commands', 'команди'])
def commands(message):
    bot.send_message(message.chat.id, 'if you want a picture of a cute animal /morepaws'
                                      '\nCommands for working with the phonebook \n/stats, /add, /delete, /list, /show')


def get_random_cat_phrase():
    cat_phrases = [
        "Готуйся, бо пушистики атакують! 🐾😺",
        "З пухнастиками настрій завжди на висоті! 😸🐾",
        "Пухнастість кота - це не просто шерсть, це мистецтво! 🐈🎨",
        "Котики - це маленькі завойовники, готові підкорити світ. 🌎🐱",
        "Пушистики відкривають доступ до світу суперпозитиву! 🌟🐾",
        "Коти - це живі витвори мистецтва з безмежним запасом пухнастості. 🎨🐈",
        "Пушистики знають, як вивести посмішку на будь-якому обличчі! 😺🥰",
        "Чарівна сила котячої пухнастості - це найпотужніший стимулятор щастя. 🐾✨",
        "Ласка котика - і радість відразу росте удвічі, а може й більше! 😻🎉",
        "Ласка котика - це термінатор для поганих настроїв. 🐱🚀",
        "Як тільки ви гладите котика, один котик у світі щасливий. 😸❤️",
        "Котик котику котик. 🐱🐾"
    ]
    return random.choice(cat_phrases)


@bot.message_handler(commands=['morepaws'])
def send_cute_animal(message):
    image_files = os.listdir('images')
    if image_files:
        random_image_file = random.choice(image_files)
        image_path = os.path.join('images', random_image_file)
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "No images found in the folder.")

    random_phrase = get_random_cat_phrase()
    bot.send_message(message.chat.id, random_phrase)


@bot.message_handler(commands=['stats'])
def stats(message):
    count = len(phone_book)
    bot.send_message(message.chat.id, f"I have {count} numbers in my phone book.")

@bot.message_handler(commands=['add'])
def add_contact(message):
    msg = bot.send_message(message.chat.id, "Enter the name for the new contact:")
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    name = message.text
    if name in phone_book:
        bot.send_message(message.chat.id, f"The contact '{name}' already exists.")
    else:
        msg = bot.send_message(message.chat.id, "Enter the phone number for the new contact:")
        bot.register_next_step_handler(msg, process_number_step, name)

def process_number_step(message, name):
    number = message.text
    if not validate_phone_number(number):
        bot.send_message(message.chat.id, "Invalid phone number format. Please try again.")
        return
    phone_book[name] = number
    with open('phone_book.json', 'w') as file:
        json.dump(phone_book, file)
    bot.send_message(message.chat.id, f"Contact '{name}' with phone number '{number}' has been added.")

@bot.message_handler(commands=['delete'])
def delete_contact(message):
    msg = bot.send_message(message.chat.id, "Enter the name of the contact you want to delete:")
    bot.register_next_step_handler(msg, process_delete_step)

def process_delete_step(message):
    name = message.text
    if name in phone_book:
        del phone_book[name]
        with open('phone_book.json', 'w') as file:
            json.dump(phone_book, file)
        bot.send_message(message.chat.id, f"Contact '{name}' has been deleted.")
    else:
        bot.send_message(message.chat.id, f"No contact named '{name}' found.")

@bot.message_handler(commands=['list'])
def list_contacts(message):
    contacts = "\n".join(phone_book.keys())
    bot.send_message(message.chat.id, f"Contacts:\n{contacts}")

@bot.message_handler(commands=['show'])
def show_contact(message):
    msg = bot.send_message(message.chat.id, "Enter the name of the contact you want to see:")
    bot.register_next_step_handler(msg, process_show_step)

def process_show_step(message):
    name = message.text
    if name in phone_book:
        number = phone_book[name]
        bot.send_message(message.chat.id, f"Contact '{name}': {number}")
    else:
        bot.send_message(message.chat.id, f"No contact named '{name}' found.")

bot.polling(none_stop=True)