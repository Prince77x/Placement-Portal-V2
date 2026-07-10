from flask import Flask
from models import db
from config import config
from extension import jwt, login_manager

app = Flask(__name__)
# app configuration 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config.from_object(config)

# Initializing 
jwt.init_app(app) # jwt token with flask 
login_manager.init_app(app) #loginmanager with flask 
db.init_app(app) #database with flask 
with app.app_context(): 
    db.create_all()



# final main app execution 
if __name__ =="__main__":
    app.run(debug=True) # to make it production level we have to remove or make debug == false