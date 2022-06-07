import flask
import flask_cors

from routes.mealRoutes import meal_routes

flask_app = flask.Flask(__name__)
flask_app.config['CORS_HEADERS'] = 'Content-Type'
flask_cors.CORS(flask_app)

meal_routes(flask_app)


flask_app.run(debug = True)