import sqlite3
connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()
print(cursor)

# query = '''
# CREATE TABLE users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     first_name TEXT,
#     last_name TEXT,
#     age INTEGER
# )
# '''
#
# cursor.execute(query)
# connection.commit()

# data = [
#     ("Vitalii", "Johnson", 36),
#     ("Oleksii", "Davidson", 32),
#     ("Oleg", "Linkoln", 34),
#     ("Olia", "Holmes", 35),
#     ("Ira", "Zelinski", 36),
# ]
#
# query = "INSERT INTO users (first_name,last_name, age) VALUES (?, ?, ?)"
# cursor.executemany(query, data)
# connection.commit()
