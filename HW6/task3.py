# Знайти найбільший елемент масиву
# — використати built-in функцію
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(a))

# — створити свою функцію
def largest_number(number, n):
    max_number = number[0]
    for num in range(1, n):
        if number[num] > max_number:
            max_number = number[num]
    return max_number


number = [1, 5, 6, 13, 4]
n = len(number)
print(largest_number(number, n))