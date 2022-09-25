from controllers import plannerController
from flask import request


def planner_routes(flask_app):

    @flask_app.route('/planner', methods=['GET'])
    def get_planned():
        return plannerController.get_planned()

    @flask_app.route('/planner/<int:user_id>', methods=['GET'])
    def get_plannedByUser(user_id):
        return plannerController.get_planned_by_user(user_id)

    @flask_app.route('/planner', methods=['PUT'])
    def add_planned():
        content = request.json
        user = content.get("user")
        meal_id = content.get("meal_id")
        return plannerController.add_planned(user, meal_id)

    @flask_app.route('/planner/<int:meal_id>', methods=['PUT'])
    def update_planned(meal_id):
        content = request.json
        name = content.get("name")
        description = content.get("description")
        times_made = content.get("times_made")
        last_made = content.get("last_made")
        rating = content.get("rating")
        online_url = content.get("online_url")
        image_url = content.get("image_url")
        user = content.get("user")
        tag_ids = content.get("tag_ids")
        return plannerController.update_meal(meal_id, name, description, times_made, last_made, rating, user, online_url, image_url, tag_ids)

    @flask_app.route('/meal/<int:meal_id>', methods=['DELETE'])
    def delete_planned(meal_id):
        return plannerController.delete_meal(meal_id)
