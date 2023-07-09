from flask import Flask, render_template, request, redirect, session, abort
# from logging.config import dictConfig
import logging
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from config import AppConfig
load_dotenv()

# dictConfig({
#     'version': 1,
#     'formatters': {'default': {
#         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#     }},
#     'handlers': {'wsgi': {
#         'class': 'logging.StreamHandler',
#         'stream': 'ext://flask.logging.wsgi_errors_stream',
#         'formatter': 'default'
#     }},
#     'root': {
#         'level': 'INFO',
#         'handlers': ['wsgi']
#     }
# })
db = SQLAlchemy()
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.config.from_object(AppConfig)
db.init_app(app)


from views import *
from models import *

# create tables
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host=app.config.get('HOST'),
            port=app.config.get('PORT'),
            debug=app.config.get('DEBUG'))