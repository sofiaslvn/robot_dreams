from app import app
from flask import Flask, request, redirect, abort


@app.route('/users', methods=['GET'])
def get_users():
    names = ['Andrew', 'Olga', 'Katerina', 'Dmytro', 'Volodymyr']
    return str(names)


@app.route('/books', methods=['GET'])
def get_books():
    books = ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5']
    book_list = '<ul>'
    for book in books:
        book_list += '<li>' + book + '</li>'
    book_list += '</ul>'
    return book_list


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id % 2 == 0:
        return f'Text with id: {user_id}'
    else:
        abort(404, 'Not Found')


@app.route('/books/<string:title>', methods=['GET'])
def get_book(title):
    transformed_title = title.capitalize()
    return transformed_title


@app.route('/params', methods=['GET'])
def get_params():
    param_table = '<table>'
    param_table += '<tr><th>Parameter</th><th>Value</th></tr>'
    for key, value in request.args.items():
        param_table += f'<tr><td>{key}</td><td>{value}</td></tr>'
    param_table += '</table>'
    return param_table


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        login_form = '''
            <form method="POST" action="/login">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required><br>
                <input type="submit" value="Submit">
            </form>
        '''
        return login_form
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return redirect('/users')
        else:
            abort(400, 'Username or password missing')


if __name__ == '__main__':
    app.run()