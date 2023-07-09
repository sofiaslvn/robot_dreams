from app import app
from flask import abort
from models import User, Book, Purchase


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [user.to_dict() for user in users]
    return {'users': user_list}

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user.to_dict()
    else:
        return abort(404, 'Користувача не знайдено')

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = [book.to_dict() for book in books]
    return {'books': book_list}

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return book.to_dict()
    else:
        return abort(404, 'Книгу не знайдено')

@app.route('/purchases', methods=['GET'])
def get_purchases():
    purchases = Purchase.query.all()
    purchase_list = [purchase.to_dict() for purchase in purchases]
    return {'purchases': purchase_list}

@app.route('/purchases/<int:purchase_id>', methods=['GET'])
def get_purchase(purchase_id):
    purchase = Purchase.query.get(purchase_id)
    if purchase:
        return purchase.to_dict()
    else:
        return abort(404, 'Покупку не знайдено')