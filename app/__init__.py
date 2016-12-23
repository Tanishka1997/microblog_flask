from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenId
from config import basdir
app=Flask(__name__)
app.config.from_object('config')
db=SQLAlchemy(app)
lm=LoginManager()
lm.init_app(app)
oid=OpenId(app,os.path.join(basedir,'tmp'))
from app import views,models
