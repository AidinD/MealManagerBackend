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

    @flask_app.route('/planner/<int:planner_id>', methods=['PUT'])
    def update_planned(planner_id):
        content = request.json
        meal_id = content.get("meal_id")
        completed = content.get("completed")

        return plannerController.update_planned(planner_id, meal_id, completed)

    @flask_app.route('/planner/<int:planner_id>', methods=['DELETE'])
    def delete_planned(planner_id):
        return plannerController.delete_planned(planner_id)

    @flask_app.route('/plannerall/<int:user_id>', methods=['DELETE'])
    def delete_AllUserPlanned(user_id):
        return plannerController.delete_all_planned_by_user(user_id)
