import json
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from sqlalchemy import inspect

db = SQLAlchemy()


class Serializer:
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def as_dict_list(l):
        return [m.as_dict() for m in l]
    pass

    @staticmethod
    def as_response_json(data, code=200):
        return jsonify(status=code, data=data)
    pass

    @staticmethod
    def obj_to_dict(obj):
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

    @staticmethod
    def flatten_join(tup_list):
        return [{**a.as_dict(), **b.as_dict()} for a, b in tup_list]
