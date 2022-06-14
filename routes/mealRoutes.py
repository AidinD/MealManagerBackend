from controllers import mealController
from flask import request


def meal_routes(flask_app):

    @flask_app.route('/meals', methods=['GET'])
    def get_meals():
        return mealController.get_meals()

    @flask_app.route('/meal/<int:meal_id>', methods=['GET'])
    def get_meal(meal_id):
        return mealController.get_meal(meal_id)

    @flask_app.route('/meal', methods=['POST'])
    def add_meal():
        print(request.form["name"])
        name = request.form["name"]
        description = request.form["description"]
        times_made = request.form["times_made"]
        last_made = request.form["last_made"]
        ranking = request.form["ranking"]
        online_url = request.form["online_url"]
        image_url = request.form["image_url"]
        user = request.form["user"]
        return mealController.add_meal(name, description, times_made, last_made, ranking, user, online_url, image_url)

    @flask_app.route('/meal/<int:meal_id>', methods=['PUT'])
    def update_meal(meal_id):
        name = request.form["name"]
        description = request.form["description"]
        times_made = request.form["times_made"]
        last_made = request.form["last_made"]
        ranking = request.form["ranking"]
        online_url = request.form["online_url"]
        image_url = request.form["image_url"]
        user = request.form["user"]
        return mealController.update_meal(meal_id, name, description, times_made, last_made, ranking, user, online_url, image_url)

    @flask_app.route('/meal/<int:meal_id>', methods=['DELETE'])
    def delete_meal(meal_id):
        return mealController.delete_meal(meal_id)
