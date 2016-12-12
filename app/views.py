from app import app
from flask import render_template,flash,redirect
from .forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Tanishka'}
	return render_template('index.html',title='Home',user=user)

@app.route('/login',methods=['GET','POSTS'])
def login():
	form=LoginForm()
	return render_template('login.html',title='Sign In',form=form)
