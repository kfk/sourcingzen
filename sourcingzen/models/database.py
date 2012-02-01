from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
from sourcingzen import app

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////home/alessio/projects/sourcingzen/test.db'
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(120))
	role = db.Column(db.String(20))

	def __init__(self, email):
		self.email = email
		self.password = password
		self.role = role

	def __repr__(self):
		return self.email, self.password, self.role

class ContactMessage(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120))
	contact_message=db.Column(db.String(1000))

	def __init__(self,email, contact_message):
		self.email=email
		self.contact_message=contact_message
	
	def __repr__(self):
		return '<email %r, contact_message %r>' % (self.email, self.contact_message)

