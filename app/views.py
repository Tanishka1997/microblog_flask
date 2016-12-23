from app import app
from flask import render_template,flash,redirect,session.url_for,request,g
from flask_login import login_user,logout_user,current_user,logout_required
from .forms import LoginForm
from app import lm,db,oid
from models import User
@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Tanishka'}
	return render_template('index.html',title='Home',user=user)

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))


@app.route('/login',methods=['GET','POST'])
def login():
	form=LoginForm()
	if g.user is not NONE and g.user.is_authenticated
	 	return redirect(url_for('index'))

	if form.validate_on_submit():
		session['remember_me']=form.remember_me.data
		return oid.try_login(form.openid.data,ask_for=['nickname','email'])

	return render_template('login.html',title='Sign In',form=form,providers=app.config['OPENID_PROVIDERS'])
