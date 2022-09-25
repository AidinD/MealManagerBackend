from models.mealModel import Meal
from models.shared import db, Serializer
from sqlalchemy.sql import func
from models.userModel import User


class Planner(db.Model, Serializer):
    fields = ['id', 'user', 'meal_id', 'completed', 'created_at', 'updated_at']

    def __init__(self, user, meal_id, completed):
        self.meal_id = meal_id
        self.user = user
        self.completed = completed
        self.created_at = func.now()
        self.updated_at = func.now()

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey(Meal.id), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime(
        timezone=True), nullable=False, onupdate=func.now(), server_default=func.now())

    meal = db.relationship("Meal", backref="planner", uselist=False)
    pass
