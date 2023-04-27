# Написати програму, яка буде:
# зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
# знаходити всі email в тексті і змінювати їх на *@*.
import re
filename = input('Please, enter filename: ')
with open(filename, 'r') as f:
    text = f.read()

matches = re.findall(r'\b\S+@\S+\.\S+\b', text)
for match in matches:
        text = text.replace(match, '*@*')

print(text)