from app import app
from models import db, Admin
from werkzeug.security import generate_password_hash

with app.app_context():
     
    if not Admin.query.first():
        admin1 = Admin(name='admin1',email='admin1@gmail.com',password=generate_password_hash('admin123'))
        admin2 = Admin(name='admin2',email='admin2@gmail.com',password=generate_password_hash('admin321'))

        db.session.add_all([admin1,admin2])
        db.session.commit()
        print('Admin data seeded')
'''

    admin1 = Admin.query.filter_by(name='admin1').first()
    db.session.delete(admin1)
    db.session.commit()
    print('data deleted')

''' 