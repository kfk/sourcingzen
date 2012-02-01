from flask import session, abort
from functools import wraps

def authorization(role):
	def decorator(f):
		def inner(*a, **kw):
			if not session.get('logged_in_as'):
				abort(401)
			elif session['logged_in_as'] == role:
				return f(*a, **kw)
			else:
				abort(401)
		return inner
	return decorator

'''
def authorization(f):
	#session['logged_in_as']
	def decorator(*args, **kwargs):
		return f
		if not session.get('logged_in_as'):
			abort(401)
		elif session['logged_in_as']==role:
			return f
		else:
			abort(401)
	return decorator
'''
'''
def logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('logged_in') is not None:
            return f(*args, **kwargs)
        else:
            flash('Please log in first...', 'error')
            next_url = get_current_url() # However you do this in Flask
            login_url = '%s?next=%s' % (url_for('login'), next_url)
            return redirect(login_url)
    return decorated_function
'''
