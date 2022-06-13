from time import timezone
from models.shared import db, Serializer
from sqlalchemy.sql import func
from models.userModel import User

class Meal(db.Model, Serializer):
    fields = ['id', 'name', 'description', 'times_made', 'last_made', 'ranking', 'online_url', 'image', 'user', 'created_at', 'updated_at']
    
    def __init__(self, name, description, times_made, last_made, ranking, user, online_url, image_url):
        self.name = name
        self.description = description
        times_made = times_made
        last_made = last_made
        self.ranking = ranking
        self.online_url = online_url
        self.image_url = image_url
        self.user = user
        self.created_at = func.now()
        self.updated_at = func.now()
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, server_default='')
    description = db.Column(db.String(300), nullable=False, server_default='')
    times_made = db.Column(db.Integer, nullable=False, server_default='0')
    last_made = db.Column(db.DateTime(timezone = True) , nullable=False, server_default=func.now())
    ranking = db.Column(db.Integer, nullable=False, server_default='3')
    online_url = db.Column(db.String(300), nullable=False, server_default='')
    image_url = db.Column(db.String(300), nullable=False, server_default='')
    user = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    created_at = db.Column(db.DateTime(timezone = True), nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone = True), nullable=False, onupdate=func.now(), server_default=func.now())    
    pass



