from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class TripModel(db.Model):
    __tablename__ = "table"
    self.trip_info = trip_info
    name = db.Column(db.String())
    length = db.Column(db.Integer())
    location = db.Column(db.String(80))
 
    def __init__(self, trip_info, name, length, location):
        self.trip_info = trip_info
        self.name = name
        self.length = length
        self.location = location
 
    def __repr__(self):
        return f"{self.name}:{self}"