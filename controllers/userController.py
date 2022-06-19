from sqlalchemy import exc
from flask import Response

from models.userModel import User
from models.shared import Serializer, db


def get_users():
    try:
        users = User.query.all()
        if(not users or users is None):
            return Serializer.as_response_json([], 204), 200
        return Serializer.as_response_json(Serializer.as_dict_list(users), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def get_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()
        if(not user or user is None):
            return Serializer.as_response_json([], 204), 200
        return Serializer.as_response_json(user.as_dict_list(), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def get_user_by_name(name):
    try:
        user = User.query.filter_by(name=name).first()
        if(user is None):
            return Serializer.as_response_json([], 204), 200
        return Serializer.as_response_json(user.as_dict(), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def add_user(name, share):
    try:
        if(not name or name == ""):
            data = {'message': 'Name cannot be empty'}
            return Serializer.as_response_json(data, 400), 400

        user = User(name, share)
        db.session.add(user)
        db.session.commit()
        return Serializer.as_response_json(user.as_dict(), 200), 200
    except exc.IntegrityError as e:
        data = {'message': 'User already exists'}
        return Serializer.as_response_json(data, 400), 400
    except exc.SQLAlchemyError as e:
        return Serializer.as_response_json(str(e), 500), 500


def update_user(user_id, name, share):
    try:
        if(not name or name == ""):
            data = {'message': 'Name cannot be empty'}
            return Serializer.as_response_json(data, 400), 400

        user = User.query.filter_by(id=user_id).first()
        if(not user or user is None):
            return Serializer.as_response_json([], 204), 200

        user.name = name
        user.share = share
        db.session.commit()
        return Serializer.as_response_json(user.as_dict(), 200), 200
    except exc.IntegrityError as e:
        data = {'message': 'Name already exists'}
        return Serializer.as_response_json(data, 400), 400
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def delete_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()
        if(user is None):
            return Serializer.as_response_json([], 204), 200
        db.session.delete(user)
        db.session.commit()
        return Serializer.as_response_json(user.as_dict(), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500
