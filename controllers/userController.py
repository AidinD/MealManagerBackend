from models.userModel import User
from flask import jsonify


from models.shared import Serializer


def get_users():
    try:
        users = User.query.all()
        if(users is None):
            return Serializer.as_response_json([], 204)
        return Serializer.as_response_json(Serializer.as_dict_list(users))
    except Exception as e:
        return Serializer.as_response_json(e, 500)


def get_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()
        if(user is None):
            return Serializer.as_response_json([], 204)
        return Serializer.as_response_json(user.as_dict(), 200)
    except Exception as e:
        return Serializer.as_response_json(e, 500)
