# 1. Написати функцію, яка повертає тільки однакові елементи двох множин.
# 2. Написати функцію, яка повертає тільки унікальні елементи двох множин.

set_1 = {1, 2, 3, 4, 5, 13}
set_2 = {3, 4, 5, 6, 7, 13}

same_elements = set_1.intersection(set_2)
print(same_elements)

unique_elements = set_1.symmetric_difference(set_2)
print(unique_elements)