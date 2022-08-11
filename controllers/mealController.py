import json
from pprint import PrettyPrinter
from models.mealModel import Meal
from models.shared import Serializer, db
from sqlalchemy import exc
from models.tagModel import Tag


def get_meals():
    try:
        meals = Meal.query.all()
        mealTags = []

        for meal in meals:
            mealJson = meal.as_dict()
            tagJson = Serializer.as_dict_list(meal.tags)

            mealTag = {**mealJson, **{'tags': tagJson}}
            mealTags.append(mealTag)

        if(meals is None):
            return Serializer.as_response_json([], 204), 204
        return Serializer.as_response_json(mealTags, 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def get_meal(meal_id):
    try:
        meal = Meal.query.filter(Meal.id == meal_id).first()

        mealJson = meal.as_dict()
        tagJson = Serializer.as_dict_list(meal.tags)

        mealTag = {**mealJson, **{'tags': tagJson}}

        if(mealTag is None):
            return Serializer.as_response_json([], 204), 204
        return Serializer.as_response_json(mealTag, 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def add_meal(name, description, rating, user, online_url, image_url, tag_ids):
    try:
        if(not name or name == ""):
            data = {'message': 'Name cannot be empty'}
            return Serializer.as_response_json(data, 400), 400
        meal = Meal(name, description, rating,
                    user, online_url, image_url)

        tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
        meal.tags.extend(tags)

        db.session.add(meal)
        db.session.commit()
        return Serializer.as_response_json(meal.as_dict(), 200), 200
    except exc.IntegrityError as e:
        data = {'message': 'Meal already exists'}
        return Serializer.as_response_json(data, 400), 400
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def update_meal(meal_id, name, description, times_made, last_made, rating, user, online_url, image_url, tag_ids):
    try:
        if(not name or name == ""):
            data = {'message': 'Name cannot be empty'}
            return Serializer.as_response_json(data, 400), 400

        meal = Meal.query.filter_by(id=meal_id).first()
        if(meal is None):
            return Serializer.as_response_json([], 204), 204
        tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
        meal.tags = tags

        meal.name = name
        meal.description = description
        meal.times_made = times_made
        meal.last_made = last_made
        meal.rating = rating
        meal.online_url = online_url
        meal.image_url = image_url
        meal.user = user
        db.session.commit()
        return Serializer.as_response_json(meal.as_dict(), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def delete_meal(meal_id):
    try:
        meal = Meal.query.filter_by(id=meal_id).first()
        if(meal is None):
            return Serializer.as_response_json([], 204), 204
        db.session.delete(meal)
        db.session.commit()
        return Serializer.as_response_json(meal.as_dict(), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500
