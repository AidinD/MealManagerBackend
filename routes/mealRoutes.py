from controller import mealController

def meal_routes(flask_app):

    @flask_app.route('/meals', methods=['GET'])
    def get_meals():
        return mealController.get_meals()

    @flask_app.route('/meal/<int:meal_id>', methods=['GET'])
    def get_meal(meal_id):
        return mealController.get_meal(meal_id)