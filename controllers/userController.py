from flask import jsonify
from models.userModel import User
from models.shared import db

from models.shared import Serializer

def get_users():
        users = User.query.all()
        if(users is None):
            return jsonify([])
        return jsonify(users = Serializer.as_dict_list(users))