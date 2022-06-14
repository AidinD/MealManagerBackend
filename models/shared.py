from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

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
        return jsonify({'status': code, 'data': data})
    pass
