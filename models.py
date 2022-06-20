import traceback
from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class TripModel(db.Model):
    __tablename__ = "table"
 
    name = db.Column(db.String())
    length = db.Column(db.Integer())
    location = db.Column(db.String(80))
 
    def __init__(self,name, length, location):
        self.name = name
        self.length = length
        self.location = location
 
    def __repr__(self):
        return f"{self.name}:{self}"