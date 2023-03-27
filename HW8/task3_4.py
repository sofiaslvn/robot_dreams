# 3. Перетворити всі елементи списку типу string в верхній регістр, використовуючи map.
# 4. Вивести всі елементу масиву, які є числом, використовуючи filter.
def uppercase(word):
    if type(word) == str:
        print(str(word).upper())
    return str(word).upper()


new_list = [1, 2, "alex", "apple", 567, 3.4, "new"]
new_words = map(uppercase, new_list)
print(list(new_words))


new_set = set([1, 2, "alex", "apple", 567, 34, "new"])
def check(x):
    if type(x) == int:
        return True
    else:
        return False
checked_numbers = filter(check, new_set)
print(list(checked_numbers))