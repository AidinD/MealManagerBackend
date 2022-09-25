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


def update_planned(planner_id, meal_id, completed):
    try:
        if(not meal_id or meal_id == ""):
            data = {'message': 'Something went wrong, meal_id is empty'}

        # TODO We need to check if foreign key exists on all add and update

        plannedMeal = Planner.query.filter_by(id=planner_id).first()
        if(plannedMeal is None):
            return Serializer.as_response_json([], 204), 204

        plannedMeal.meal_id = meal_id
        plannedMeal.completed = completed

        db.session.commit()

        return Serializer.as_response_json(plannedMeal.as_dict(), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def delete_planned(planner_id):
    try:
        plannedMeal = Planner.query.filter_by(id=planner_id).first()
        if(plannedMeal is None):
            return Serializer.as_response_json([], 204), 204
        db.session.delete(plannedMeal)
        db.session.commit()
        return Serializer.as_response_json(plannedMeal.as_dict(), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def delete_all_planned_by_user(user_id):
    try:
        plannedMeals = Planner.query.filter_by(user=user_id).all()
        if(plannedMeals is None or len(plannedMeals) == 0):
            return Serializer.as_response_json([], 204), 204

        for plannedMeal in plannedMeals:
            db.session.delete(plannedMeal)
        db.session.commit()
        return Serializer.as_response_json(Serializer.as_dict_list(plannedMeals), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500
