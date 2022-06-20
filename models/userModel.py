from time import timezone
from models.shared import db, Serializer
from sqlalchemy.sql import func


class User(db.Model, Serializer):
    fields = ['id', 'name', 'created_at', 'updated_at']

    def __init__(self, name):
        self.name = name
        self.created_at = func.now()
        self.updated_at = func.now()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True,
                     nullable=False, server_default='')
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime(
        timezone=True), nullable=False, onupdate=func.now(), server_default=func.now())
    pass
