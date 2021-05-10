#~um-mid-flask/database/models.py
from .db import db

class Book(db.Document):
    author = db.StringField()
    country = db.StringField()
	imageLink = db.StringField()
	language = db.StringField()
	link = db.StringField()
	pages = db.IntegerField()
	title = db.StringField()
	year = db.IntegerField()
