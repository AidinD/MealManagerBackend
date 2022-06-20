from flask import Flask
from models.shared import db

app = Flask(__name__)

app.config.from_pyfile('config.py')

username = app.config['DB_USER']
key = app.config['DB_KEY']
host = app.config['DB_ADDRESS']
databaseName = app.config['DB_NAME']

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://' + \
    username + ':' + key + '@'+host+'/' + databaseName

db.init_app(app)


with app.app_context():
    print("Hello World")
    db.create_all()
