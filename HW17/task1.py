import sqlite3
conn = sqlite3.connect('database_1.sqlite')
cursor = conn.cursor()

# SELECT * FROM users WHERE age > 30

# SELECT COUNT(id) AS count FROM users WHERE age > 30

# SELECT age, COUNT(id) AS users
# FROM users
# WHERE age > 30
# GROUP BY age

# SELECT age, COUNT(id) AS users
# FROM users
# WHERE age > 30
# GROUP BY age
# ORDER BY users DESC, age ASC

# SELECT age, users
# FROM (
#     SELECT age, COUNT(id) AS users
#     FROM users
#     WHERE age > 30
#     GROUP BY age
#     HAVING users > 1
#      )
# ORDER BY users DESC, age ASC;