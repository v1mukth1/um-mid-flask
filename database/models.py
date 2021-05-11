#~um-mid-flask/database/models.py
from .db import db

class Books(db.Document):
	__tablename__ = "books"
	id = db.IntField(primary_key=True)
	author = db.StringField()
	country = db.StringField()
	imageLink = db.StringField()
	language = db.StringField()
	link = db.StringField()
	pages = db.IntField()
	title = db.StringField()
	year = db.IntField()
