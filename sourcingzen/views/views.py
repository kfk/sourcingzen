from flask import render_template, request
from sourcingzen import app
from sourcingzen.models.database import db, User, ContactMessage
from sourcingzen.modules.zen_auth import authorization

#FORM
from wtforms import Form, BooleanField, TextField, TextAreaField, PasswordField, validators

class RegistrationForm(Form):
	email = TextField('Email Address', [validators.Length(min=6, max=50),validators.Email()])

class ContactForm(Form):
	email = TextField('Email Address', [validators.Length(min=6, max=50), validators.Email()])
	contact_message = TextAreaField('Contact Message', [validators.Length(min=20, max=1000)])
#/FORM

#VIEWS
@app.route('/tests/')
def tests():
	db.create_all()
	db.session.commit()
	return '1'

@app.route('/')
def index():
	form=RegistrationForm(request.form)
	email_field= form.email(class_="content_email_input")
	return render_template('index.html',email_field=email_field)

@app.route('/features')
def features():
	return render_template('features.html')

@app.route('/contact', methods=['POST','GET'])
def contact():
	form=ContactForm(request.form)
	email=form.email(class_="content_email_input")
	contact_message=form.contact_message(class_="contact")
	if request.method=='POST':
		if form.validate():
			#Add to DB
			contact_message=ContactMessage(form.email.data,form.contact_message.data)
			db.session.add(contact_message)
			db.session.commit()
			#/Add to DB
			message="Your message has been sent, thanks for your attention."
		else:
			message="Your message could not validate. Please, check if you entered a message longer than 20 characters or if you entered a correct email address."
		return render_template('submitted.html',message=message)
	return render_template('contact.html',email=email,contact_message=contact_message)

@app.route('/email_submitted', methods=['POST','GET'])
def email_submitted():
	form=RegistrationForm(request.form)
	if request.method=='POST' and form.validate():
		if form.email.data in map(str,User.query.all()):
			message="This email was already entered."
		else:
			#Add to DB
			user=User(form.email.data)
			db.session.add(user)
			db.session.commit()
			#/Add to DB
			message="Congratulations! You subscribed for an invitation to the free beta of Sourcing Zen. Thanks."
		return render_template('submitted.html',message=message)
	else:
		message="Something went wrong. Please, check you are entering a correct email."
		return render_template('submitted.html',message=message)

@app.route('/admin/users')
@authorization(role='suadmin')
def get_users():
	users=User.query.all()
	out=''
	for i in range(len(users)):
		out+=users[i].email
	return out

@app.route('/admin/contact_messages')
@authorization(role='suadmin')
def get_contact_messages():
	contact_messages=ContactMessage.query.all()
	print contact_messages
	out=''
	for i in range(len(contact_messages)):
		out+=contact_messages[i].email + ' and ' + contact_messages[i].contact_message
	return out
