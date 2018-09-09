from app import db
from flask_sqlalchemy import SQLAlchemy

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.String(128), Index = True, Unique = False)
    release = db.Column(db.)
