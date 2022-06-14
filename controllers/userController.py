from models.userModel import User
from models.shared import Serializer, db


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


def add_user(name, share):
    response = get_user_by_name(name)
    if(response.status_code == 200):
        try:
            user = User(name, share)
            db.session.add(user)
            db.session.commit()
            return Serializer.as_response_json(user.as_dict(), 200)
        except Exception as e:
            return Serializer.as_response_json(e, 500)
    else:
        data = {'message': 'User already exists'}
        return Serializer.as_response_json(data, 400)


def update_user(user_id, name, share):
    response = get_user_by_name(name)
    if(response.status_code == 200):
        try:
            user = User.query.filter_by(id=user_id).first()
            if(user is None):
                return Serializer.as_response_json([], 204)
            user.name = name
            user.share = share
            db.session.commit()
            return Serializer.as_response_json(user.as_dict(), 200)
        except Exception as e:
            return Serializer.as_response_json(e, 500)
    else:
        data = {'message': 'User already exists'}
        return Serializer.as_response_json(data, 400)


def delete_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()
        if(user is None):
            return Serializer.as_response_json([], 204)
        db.session.delete(user)
        db.session.commit()
        return Serializer.as_response_json(user.as_dict(), 200)
    except Exception as e:
        return Serializer.as_response_json(e, 500)


def get_user_by_name(name):
    try:
        user = User.query.filter_by(name=name).first()
        if(user is None):
            return Serializer.as_response_json([], 204)
        return Serializer.as_response_json(user.as_dict(), 200)
    except Exception as e:
        return Serializer.as_response_json(e, 500)
