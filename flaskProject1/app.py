from flask import Flask
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    app.logger.info('Handling / endpoint')
    return (
        '<h1>Hello World!</h1>'
    )

@app.route('/html')
def html_endpoint():
    app.logger.info('Handling /html endpoint')
    return '''
        <html>
            <body>
                <h1>This is an HTML endpoint</h1>
            </body>
        </html>
    '''

@app.route('/json')
def json_endpoint():
    app.logger.info('Handling /json endpoint')
    return {
        'message': 'This is a JSON endpoint',
        'data': {
            'name': 'Jane',
            'age': 25
        }
    }

if __name__ == '__main__':
    app.run(debug=True)