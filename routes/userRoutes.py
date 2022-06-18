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
    def get_user_by_name(name):
        return userController.get_user_by_name(name)

    @flask_app.route('/user', methods=['PUT'])
    @cross_origin(origin='*', headers=['Content-Type', 'allow-headers'])
    def add_user():
        print()
        name = request.form.get("name")
        share = request.form.get("share")
        return userController.add_user(name, share)

    @flask_app.route('/user/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        name = request.form["name"]
        share = request.form["share"]
        return userController.update_user(user_id, name, share)

    @flask_app.route('/user/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        return userController.delete_user(user_id)
