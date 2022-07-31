from models.tagModel import Tag
from models.shared import Serializer, db
from sqlalchemy import exc


def get_tags():
    try:
        tags = Tag.query.all()
        if(tags is None):
            return Serializer.as_response_json([], 204), 204
        return Serializer.as_response_json(Serializer.as_dict_list(tags), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def get_tag(tag_id):
    try:
        tag = Tag.query.filter_by(id=tag_id).first()
        if(tag is None):
            return Serializer.as_response_json([], 204), 204
        return Serializer.as_response_json(tag.as_dict(), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def add_tag(name, user, color):
    try:
        if(not name or name == ""):
            data = {'message': 'Name cannot be empty'}
            return Serializer.as_response_json(data, 400), 400
        tag = Tag(name, user, color)

        db.session.add(tag)
        db.session.commit()
        return Serializer.as_response_json(tag.as_dict(), 200), 200
    except exc.IntegrityError as e:
        data = {'message': 'Tag already exists'}
        return Serializer.as_response_json(data, 400), 400
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def update_tag(tag_id, name, user, color):
    try:
        tag = Tag.query.filter_by(id=tag_id).first()
        if(tag is None):
            return Serializer.as_response_json([], 204), 204
        tag.name = name
        tag.user = user
        tag.color = color
        db.session.commit()
        return Serializer.as_response_json(tag.as_dict(), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500


def delete_tag(tag_id):
    try:
        tag = Tag.query.filter_by(id=tag_id).first()
        if(tag is None):
            return Serializer.as_response_json([], 204), 204
        db.session.delete(tag)
        db.session.commit()
        return Serializer.as_response_json(tag.as_dict(), 200), 200
    except Exception as e:
        return Serializer.as_response_json(str(e), 500), 500
