from flask import request, render_template, session, flash, redirect
from sourcingzen import app
from sourcingzen.models.database import User
from sourcingzen.modules.zen_auth import authorization

def get_user(email):
	user = User.query.filter_by(email=email).first()
	return user

@app.route('/login_test')
@authorization(role='suadmin')
def test_():
	return 'hello'

#TODO: Use WTF
@app.route('/login', methods=['GET', 'POST'])
def login():	
	error = None
	if request.method == 'POST':
		user=get_user(request.form['username'])
		if request.form['username'] != user.email:
			error = 'Invalid username'
		elif request.form['password'] != user.password:
			error = 'Invalid password'
		else:
			session['logged_in_as'] = user.role
			flash('You were logged in')
			return redirect('/')
	return render_template('/login/login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in_as', None)
    flash('You were logged out')
    return redirect('/')



