# Написати програму, яка буде:
# зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
# знаходити всі email в тексті і змінювати їх на X***@****X, де замість Х мають бути перша і остання літери
# справжньої адреси, а весь інший текст має бути замінений на *. Кількість * необовʼязково має відповідати
# кількості замінених символів

import re
filename = input('Please, enter filename: ')
with open(filename, 'r') as f:
    text = f.read()

matches = re.findall(r'\b\S+@\S+\.\S+\b', text)
for match in matches:
    first_char = match[0]
    last_char = match.split('@')[0][-1]
    new_email = first_char + '***@***' + last_char
    text = text.replace(match, new_email)

print(text)