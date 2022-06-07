import flask

def get_meals():
        return flask.jsonify({"meals": [
            {"id": 1, "name": "Pizza", "price": 10.0},
            {"id": 2, "name": "Burger", "price": 15.0},
            {"id": 3, "name": "Pasta", "price": 12.0}
        ]})

def get_meal(meal_id):
        return flask.jsonify({"meal": [
            {"id": 1, "name": "Pizza", "price": 10.0},
            {"id": 2, "name": "Burger", "price": 15.0},
            {"id": 3, "name": "Pasta", "price": 12.0}
        ][meal_id - 1]})