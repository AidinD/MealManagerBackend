from controllers import userController
from flask import request


def user_routes(flask_app):

    @flask_app.route('/users', methods=['GET'])
    def get_users():
        return userController.get_users()

    @flask_app.route('/user/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        return userController.get_user(user_id)
