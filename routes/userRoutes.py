from controllers import userController
from flask import request
from flask_cors import cross_origin


def user_routes(flask_app):

    @flask_app.route('/users', methods=['GET'])
    def get_users():
        return userController.get_users()

    @flask_app.route('/user/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        return userController.get_user(user_id)

    @flask_app.route('/user/<string:name>', methods=['GET'])
    @cross_origin()
    def get_user_by_name(name):
        return userController.get_user_by_name(name)

    @flask_app.route('/user', methods=['PUT'])
    @cross_origin()
    def add_user():
        print()
        content = request.json
        name = content.get("name")
        share = content.get("share")
        return userController.add_user(name, share)

    @flask_app.route('/user/<int:user_id>', methods=['PUT'])
    @cross_origin()
    def update_user(user_id):
        content = request.json
        name = content.get("name")
        share = content.get("share")
        return userController.update_user(user_id, name, share)

    @flask_app.route('/user/<int:user_id>', methods=['DELETE'])
    @cross_origin()
    def delete_user(user_id):
        return userController.delete_user(user_id)
