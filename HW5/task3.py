# 3. (необов'язкове виконання) Надрукувати наступний патерн, використовуючи цикл в циклі
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for x in range(1, i+1):
        print(x, end='')
    print()