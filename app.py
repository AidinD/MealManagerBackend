from flask import Flask

from models.shared import db
from routes.mealRoutes import meal_routes

flask_app = Flask(__name__)

#region Config
flask_app.config.from_pyfile('config.py')

username = flask_app.config['DB_USER']
key = flask_app.config['DB_KEY']
host = flask_app.config['DB_ADDRESS']
databaseName = flask_app.config['DB_NAME']

flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://' + username +':' +key + '@'+host+'/' + databaseName
#endregion

db.init_app(flask_app)
meal_routes(flask_app)

flask_app.run(debug = True)