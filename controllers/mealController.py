from flask import jsonify
from json import dumps
from models.mealModel import Meal
from models.shared import db

from models.shared import Serializer

def get_meals():
        meals = Meal.query.all()
        if(meals is None):
            return dumps([])
        return jsonify(meals = Serializer.as_dict_list(meals))

def get_meal(meal_id):
        meal = Meal.query.filter_by(id=meal_id).first()
        if(meal is None):
            return dumps([])
        return jsonify(meal.as_dict())

def add_meal(name, description, times_made, last_made, ranking, user, online_url, image_url):
        meal = Meal(name, description, times_made, last_made, ranking, user, online_url, image_url)
        db.session.add(meal)
        db.session.commit()
        return jsonify(meal.as_dict())

def update_meal(meal_id, name, description, times_made, last_made, ranking, user, online_url, image_url):
        meal = Meal.query.filter_by(id=meal_id).first()
        if(meal is None):
            return dumps([])
        meal.name = name
        meal.description = description
        meal.times_made = times_made
        meal.last_made = last_made
        meal.ranking = ranking
        meal.online_url = online_url
        meal.image_url = image_url
        meal.user = user
        db.session.commit()
        return jsonify(meal.as_dict())

def delete_meal(meal_id):
        meal = Meal.query.filter_by(id=meal_id).first()
        if(meal is None):
            return dumps([])
        db.session.delete(meal)
        db.session.commit()
        return jsonify(meal.as_dict())
        