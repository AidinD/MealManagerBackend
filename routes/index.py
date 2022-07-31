from routes.mealRoutes import meal_routes
from routes.tagRoutes import tag_routes
from routes.userRoutes import user_routes


def routes(flask_app):
    meal_routes(flask_app)
    user_routes(flask_app)
    tag_routes(flask_app)
