from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
db = SQLAlchemy()

class Admin(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(70),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(256),nullable=False)

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(70),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(256),nullable=False)
    education = db.Column(db.String(50),nullable=False)
    skills = db.Column(db.String(100))
    resume = db.Column(db.String(300))
    is_active = db.Column(db.Boolean(), default=True)

    applications = db.relationship("Application", backref="student", lazy=True)



class Company(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String(70),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(256),nullable=False)
    discription = db.Column(db.String(300),nullable=False)
    is_approved = db.Column(db.Boolean(),default=False)
    is_active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    jobs = db.relationship('Job', backref='company',lazy=True)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drive=db.Column(db.String(8),nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    skills_required = db.Column(db.Text)
    experience_required = db.Column(db.String(50))
    salary_range = db.Column(db.String(50))
    location = db.Column(db.String(100))

    status = db.Column(db.String(20), default="Open")   # Open / Closed
    is_approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'),nullable=False)
    applications = db.relationship("Application", backref="job", lazy=True)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(30),default = 'Applied') ## Applied / Shortlisted / Interview / Rejected / Placed
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("job.id"), nullable=False)
    placement = db.relationship('Placement',backref='application',lazy= True)
    # This will prevent from applying for job againg and againg for the same post 
    __table_args__ = (
        db.UniqueConstraint('student_id', 'job_id', name='unique_application'),
    )

class Placement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    offer_date = db.Column(db.Date)
    joining_date = db.Column(db.Date)
    package = db.Column(db.String(50))

    application_id = db.Column(db.Integer, db.ForeignKey('application.id'),nullable=False,unique=True)

    