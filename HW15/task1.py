class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)

# some_bot = Bot('Marvin')
# some_bot.say_name()
# some_bot.send_message('Варенички з картоплею')

class TelegramBot(Bot):
    def __init__(self, name):
        super().__init__(name)
        self.url = None
        self.chat_id = None

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        if self.chat_id is None:
            chat = 'None'
        else:
            chat = self.chat_id

        if self.url is None:
            url = 'None'
        else:
            url = self.url
        print(f'{self.name} says {message} to {chat} using {url}')


telegram_bot = TelegramBot('TG')
telegram_bot.say_name()
telegram_bot.set_url('chat')
telegram_bot.set_chat_id(4)
telegram_bot.send_message('Варенички з картоплею')
