import sqlite3
connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()
print(cursor)

query = '''
CREATE TABLE users_unique (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    UNIQUE (first_name, last_name)
)
'''

cursor.execute(query)
connection.commit()

data = [
    ("Vitalii", "Johnson", 36),
    ("Oleksii", "Davidson", 32),
    ("Oleg", "Linkoln", 34),
    ("Olia", "Holmes", 35),
    ("Ira", "Zelinski", 36),
]

query = "INSERT INTO users_unique(first_name,last_name, age) VALUES (?, ?, ?)"
cursor.executemany(query, data)
connection.commit()