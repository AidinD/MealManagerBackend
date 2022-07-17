from controllers import mealController
from flask import request


def meal_routes(flask_app):

    @flask_app.route('/meals', methods=['GET'])
    def get_meals():
        return mealController.get_meals()

    @flask_app.route('/meal/<int:meal_id>', methods=['GET'])
    def get_meal(meal_id):
        return mealController.get_meal(meal_id)

    @flask_app.route('/meal', methods=['PUT'])
    def add_meal():
        content = request.json
        name = content.get("name")
        description = content.get("description")
        rating = content.get("rating")
        online_url = content.get("online_url")
        image_url = content.get("image_url")
        user = content.get("user")
        return mealController.add_meal(name, description, rating, user, online_url, image_url)

    @flask_app.route('/meal/<int:meal_id>', methods=['PUT'])
    def update_meal(meal_id):
        content = request.json
        name = content.get("name")
        description = content.get("description")
        times_made = content.get("times_made")
        last_made = content.get("last_made")
        rating = content.get("rating")
        online_url = content.get("online_url")
        image_url = content.get("image_url")
        user = content.get("user")
        return mealController.update_meal(meal_id, name, description, times_made, last_made, rating, user, online_url, image_url)

    @flask_app.route('/meal/<int:meal_id>', methods=['DELETE'])
    def delete_meal(meal_id):
        return mealController.delete_meal(meal_id)
