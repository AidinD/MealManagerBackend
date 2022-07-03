from flask import Flask
from models.shared import db
from models.mealModel import Meal
from models.userModel import User

app = Flask(__name__)

app.config.from_pyfile('config.py')

username = app.config['DB_USER']
password = app.config['DB_PASSWORD']
host = app.config['DB_ADDRESS']
databaseName = app.config['DB_NAME']
port = app.config['DB_PORT']
connection_string = f"mysql+mysqldb://{username}:{password}@{host}:{port}/{databaseName}"

app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

db.init_app(app)


with app.app_context():
    print("Hello World")
    db.create_all()
