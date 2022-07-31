from models.shared import db, Serializer
from sqlalchemy.sql import func
from models.userModel import User


class Tag(db.Model, Serializer):
    fields = ['id', 'name', 'user', 'color', 'created_at', 'updated_at']

    def __init__(self, name, user, color):
        self.name = name
        self.user = user
        self.color = color
        self.created_at = func.now()
        self.updated_at = func.now()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False,
                     unique=True, server_default='')
    user = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    color = db.Column(db.String(7), nullable=False, server_default='')
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime(
        timezone=True), nullable=False, onupdate=func.now(), server_default=func.now())
    pass
