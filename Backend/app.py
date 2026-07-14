from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from models import db
from config import config
from extension import jwt, login_manager
from routes.auth import auth
#from routes.admin import admin
from routes.company import company
from routes.student import student

app = Flask(__name__)
CORS(app,origins=["http://localhost:8080"])
# app configuration 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["JWT_SECRET_KEY"] = "my-super-secret-jwt-key"
print(app.config.get("JWT_SECRET_KEY"))
app.config.from_object(config)

# Initializing 
jwt.init_app(app) # jwt token with flask 
login_manager.init_app(app) #loginmanager with flask 
db.init_app(app) #database with flask 
with app.app_context(): 
    db.create_all()

# auth routes executing 
app.register_blueprint(auth)
#app.register_blueprint(admin)
app.register_blueprint(company)
app.register_blueprint(student)

# final main app execution 
if __name__ =="__main__":
    app.run(debug=True) # to make it production level we have to remove or make debug == false