from controllers import userController
from flask import request

def user_routes(flask_app):

    @flask_app.route('/users', methods=['GET'])
    def get_users():
        return userController.get_users()