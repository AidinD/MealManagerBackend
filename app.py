import flask
import flask_cors

from routes.mealRoutes import meal_routes

flask_app = flask.Flask(__name__)
flask_app.config.from_pyfile('config.py')
flask_cors.CORS(flask_app)

meal_routes(flask_app)

#flask_app.config.get('DB_ADDRESS')

flask_app.run(debug = True)