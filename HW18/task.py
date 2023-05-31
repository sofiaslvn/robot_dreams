# Написати запит, який виведе дату покупки і імʼя користувача, що її здійснив.
# SELECT purchases.id, purchases.date, users.first_name, users.last_name
# FROM purchases
# INNER JOIN users ON purchases.user_id = users.id;

# Написати запит, який виведе всіх users і назви  всіх книжок, які вони купували,
# відсортувати дані за user_id.
# SELECT users.id, users.first_name, users.last_name, books.title
# FROM users
# LEFT JOIN purchases ON users.id = purchases.user_id
# LEFT JOIN books ON purchases.book_id = books.id
# ORDER BY users.id;

# Запит, який для кожного user порахує суму всіх покупок. Результат має бути представлений у форматі:
# users.id, users.first_name, users.last_name, total_purchases
# SELECT users.id, users.first_name, users.last_name, SUM(books.price) AS total_purchases
# FROM users
# LEFT JOIN purchases ON users.id = purchases.user_id
# LEFT JOIN books ON purchases.book_id = books.id
# GROUP BY users.id;

# Запит, який виведе кількість покупок книжок для кожного user. Результат має бути представлений
# у форматі: user.id, purchases_count
# SELECT purchases.user_id AS user_id, COUNT(purchases.id) AS purchases_count
# FROM purchases
# GROUP BY purchases.user_id;

# Запит, який виведе кількість покупок книжок для автора Rowling. Результат має бути
# представлений у форматі: amount
# SELECT COUNT(purchases.id) AS amount
# FROM purchases
# INNER JOIN books ON purchases.book_id = books.id
# WHERE books.author = 'Rowling';

# Запит, який виведе загальні суми продажів для кожного автора та кількість покупок.
# SELECT books.author, SUM(books.price) AS total_sales, COUNT(purchases.id) AS purchase_count
# FROM books
# LEFT JOIN purchases ON books.id = purchases.book_id
# GROUP BY books.author;

# Запит, який виведе всі назви книжок із кількістю їх продажів в порядку спадання кількості продажів.
# SELECT books.title, COUNT(purchases.id) AS purchase_count
# FROM books
# LEFT JOIN purchases ON books.id = purchases.book_id
# GROUP BY books.title
# ORDER BY purchase_count DESC;