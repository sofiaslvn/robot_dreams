# Створити клас Bot та TelegramBot із першого завдання за допомогою функції type

def send_message(self, message):
    print(message)

def say_name(self):
    print(self.name)

Bot = type('Bot', (object,), {
    'name': '',
    'send_message': send_message,
    'say_name': say_name
})

some_bot = Bot()
some_bot.name = ('Marvin')
some_bot.say_name()
some_bot.send_message("Варенички з картоплею")

