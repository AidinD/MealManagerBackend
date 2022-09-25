from pprint import PrettyPrinter
from models.mealModel import Meal
from models.shared import Serializer, db
from sqlalchemy import exc
from models.plannerModel import Planner


def get_planned():
    try:
        plannedMeals = Planner.query.all()
        mealsPlanned = []

        for plannedMeal in plannedMeals:
            plannedMealJson = plannedMeal.as_dict()
            mealJson = plannedMeal.meal.as_dict()
            mealPlanned = {**plannedMealJson, **{'meal': mealJson}}
            mealsPlanned.append(mealPlanned)

        if(plannedMeals is None or len(plannedMeals) == 0):
            return Serializer.as_response_json([], 204), 204
        return Serializer.as_response_json(mealsPlanned, 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def get_planned_by_user(user_id):
    try:
        plannedMeals = Planner.query.filter_by(user=user_id).all()
        mealsPlanned = []

        for plannedMeal in plannedMeals:
            plannedMealJson = plannedMeal.as_dict()
            mealJson = plannedMeal.meal.as_dict()
            mealPlanned = {**plannedMealJson, **{'meal': mealJson}}
            mealsPlanned.append(mealPlanned)

        if(plannedMeals is None or len(plannedMeals) == 0):
            return Serializer.as_response_json([], 204), 204
        return Serializer.as_response_json(mealsPlanned, 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def add_planned(user, meal_id):
    print(user, meal_id)
    try:
        if(not meal_id or meal_id == ""):
            data = {'message': 'Something went wrong, meal_id is empty'}
            return Serializer.as_response_json(data, 400), 400

        plannedMeal = Planner(user, meal_id, False)

        db.session.add(plannedMeal)
        db.session.commit()
        return Serializer.as_response_json(plannedMeal.as_dict(), 200), 200
    except exc.IntegrityError as e:
        data = {'message': 'Planned meal already exists'}
        return Serializer.as_response_json(data, 400), 400
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def update_planned(meal_id, name, description, times_made, last_made, rating, user, online_url, image_url, tag_ids):
    try:
        if(not name or name == ""):
            data = {'message': 'Name cannot be empty'}

    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def delete_all_planned(meal_id):
    try:
        meal = Meal.query.filter_by(id=meal_id).first()
        if(meal is None):
            return Serializer.as_response_json([], 204), 204
        db.session.delete(meal)
        db.session.commit()
        return Serializer.as_response_json(meal.as_dict(), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def delete_planned(meal_id):
    try:
        meal = Meal.query.filter_by(id=meal_id).first()
        if(meal is None):
            return Serializer.as_response_json([], 204), 204
        db.session.delete(meal)
        db.session.commit()
        return Serializer.as_response_json(meal.as_dict(), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500
