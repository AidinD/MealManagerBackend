from flask import jsonify
from json import dumps
from models.mealModel import Meal
from models.shared import db

from models.shared import Serializer


def get_meals():
    try:
        meals = Meal.query.all()
        if(meals is None):
            return Serializer.as_response_json([], 204)
        return Serializer.as_response_json(Serializer.as_dict_list(meals), 200)
    except Exception as e:
        return Serializer.as_response_json(e, 500)


def get_meal(meal_id):
    try:
        meal = Meal.query.filter_by(id=meal_id).first()
        if(meal is None):
            return Serializer.as_response_json([], 204)
        return Serializer.as_response_json(meal.as_dict(), 200)
    except Exception as e:
        return Serializer.as_response_json(e, 500)


def add_meal(name, description, times_made, last_made, ranking, user, online_url, image_url):
    try:
        meal = Meal(name, description, times_made, last_made,
                    ranking, user, online_url, image_url)
        db.session.add(meal)
        db.session.commit()
        return Serializer.as_response_json(meal.as_dict(), 200)
    except Exception as e:
        return Serializer.as_response_json(e, 500)


def update_meal(meal_id, name, description, times_made, last_made, ranking, user, online_url, image_url):
    try:
        meal = Meal.query.filter_by(id=meal_id).first()
        if(meal is None):
            return Serializer.as_response_json([], 204)
        meal.name = name
        meal.description = description
        meal.times_made = times_made
        meal.last_made = last_made
        meal.ranking = ranking
        meal.online_url = online_url
        meal.image_url = image_url
        meal.user = user
        db.session.commit()
        return Serializer.as_response_json(meal.as_dict(), 200)
    except Exception as e:
        return Serializer.as_response_json(e, 500)


def delete_meal(meal_id):
    try:
        meal = Meal.query.filter_by(id=meal_id).first()
        if(meal is None):
            return Serializer.as_response_json([], 204)
        db.session.delete(meal)
        db.session.commit()
        return Serializer.as_response_json(meal.as_dict(), 200)
    except Exception as e:
        return Serializer.as_response_json(e, 500)
