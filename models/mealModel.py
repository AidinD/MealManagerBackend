from models.shared import db
from sqlalchemy.sql import func

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(max), nullable=False)
    times_made = db.Column(db.Integer, nullable=False, default=0)
    last_made = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    image = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())