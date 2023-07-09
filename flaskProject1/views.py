from app import app
from flask import render_template, request, redirect, session, abort


@app.route('/users', methods=['GET'])
def get_users():
    names = ['Andrew', 'Olga', 'Katerina', 'Dmytro', 'Volodymyr']
    username = session.get('username')
    return render_template('tasks/users.html', names=names, username=username)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id % 2 == 0:
        return render_template('tasks/user.html', user_id=user_id)
    else:
        abort(404, 'Not Found')


@app.route('/books', methods=['GET'])
def get_books():
    books = ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5']
    username = session.get('username')
    return render_template('tasks/books.html', books=books, username=username)


@app.route('/books/<string:title>', methods=['GET'])
def get_book(title):
    transformed_title = title.capitalize()
    username = session.get('username')
    return render_template('tasks/book.html', title=transformed_title, username=username)


@app.route('/params', methods=['GET'])
def get_params():
    params = request.args
    username = session.get('username')
    return render_template('tasks/params.html', params=params, username=username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'username' in session:
            return redirect('/users')
        return render_template('tasks/login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            session['username'] = username
            return redirect('/users')
        else:
            abort(400, 'Username or password missing')