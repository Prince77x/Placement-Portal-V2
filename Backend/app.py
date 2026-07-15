from flask import Flask, Blueprint, jsonify
from celery_app import celery

from flask_cors import CORS
from models import db
from config import config
from extension import jwt, login_manager
from routes.auth import auth
from routes.admin import admin
from routes.company import company
from routes.student import student
from routes.export import export
from cache import cache

 

app = Flask(__name__)
CORS(app,origins=["http://localhost:8080"])
# app configuration 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["JWT_SECRET_KEY"] = "my-super-secret-jwt-key"
print(app.config.get("JWT_SECRET_KEY"))
app.config.from_object(config)

# cache configurations 
app.config["CACHE_TYPE"] = "RedisCache"
app.config["CACHE_REDIS_URL"] = "redis://localhost:6379/1"
app.config["CACHE_DEFAULT_TIMEOUT"] = 60  # seconds

cache.init_app(app)

# Initializing 
jwt.init_app(app) # jwt token with flask 
login_manager.init_app(app) #loginmanager with flask 
db.init_app(app) #database with flask 
with app.app_context(): 
    db.create_all()

celery.conf.update(app.config)

class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

celery.Task = ContextTask

# auth routes executing 
app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(company)
app.register_blueprint(student)
app.register_blueprint(export)

# final main app execution 
if __name__ =="__main__":
    app.run(debug=True) # to make it production level we have to remove or make debug == false