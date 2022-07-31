from controllers import tagController
from flask import request


def tag_routes(flask_app):

    @flask_app.route('/tags', methods=['GET'])
    def get_tags():
        return tagController.get_tags()

    @flask_app.route('/tag/<int:tag_id>', methods=['GET'])
    def get_tag(tag_id):
        return tagController.get_tag(tag_id)

    @flask_app.route('/tag', methods=['PUT'])
    def add_tag():
        content = request.json
        name = content.get("name")
        user = content.get("user")
        color = content.get("color")
        return tagController.add_tag(name, user, color)

    @flask_app.route('/tag/<int:tag_id>', methods=['PUT'])
    def update_tag(tag_id):
        content = request.json
        name = content.get("name")
        user = content.get("user")
        color = content.get("color")
        return tagController.update_tag(tag_id, name, user, color)

    @flask_app.route('/tag/<int:tag_id>', methods=['DELETE'])
    def delete_tag(tag_id):
        return tagController.delete_tag(tag_id)
