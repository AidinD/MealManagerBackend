from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Serializer: 
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    @staticmethod
    def as_dict_list(l):
        return [m.as_dict() for m in l]
    pass