from flask import Flask
from models.shared import db

app = Flask(__name__)

app.config.from_pyfile('config.py')

username = app.config['DB_USER']
key = app.config['DB_KEY']
host = app.config['DB_ADDRESS']
databaseName = app.config['DB_NAME']
port = app.config['DB_PORT']
connection_string = f"mysql+mysqldb://{username}:{key}@{host}:{port}/{databaseName}"

app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

db.init_app(app)

with app.app_context():
    db.create_all()
