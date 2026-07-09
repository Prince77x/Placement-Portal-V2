from flask import Flask
from models import db


app = Flask(__name__)
# app configuration 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Initializing database with flask 
db.init_app(app)
with app.app_context(): 
    db.create_all()


# final main app execution 
if __name__ =="__main__":
    app.run(debug=True) # to make it production level we have to remove or make debug == false