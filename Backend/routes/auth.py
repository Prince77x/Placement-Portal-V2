from flask import Blueprint, jsonify,request
from werkzeug.security import generate_password_hash, check_password_hash
from models import Student,Admin,Company,db
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)

# Student Registeration route 

@auth.route("/api/student/register", methods=['POST'])
def register_student():
    # recive JSON data
    data = request.get_json()

    # Extract fields 
    name = data.get('name')
    email= data.get('email')
    password = data.get("password")
    education = data.get("education")
    skills = data.get('skills')
    resume = data.get('resume')

    # Validate required fields
    if not name or not email or not password or not education:
        return jsonify({
            "message": "All required fields must be provided."
        }), 400

    # Check if email already exists
    existing_student = Student.query.filter_by(email=email).first()

    if existing_student:
        return jsonify({
            "message": "Email already registered."
        }), 409

    # Hash password
    hashed_password = generate_password_hash(password)

    # Create student object
    student = Student(
        name=name,
        email=email,
        password=hashed_password,
        education=education,
        skills=skills,
        resume=resume
    )

    # Save into database
    db.session.add(student)
    db.session.commit()

    # Return success
    return jsonify({
        "message": "Student registered successfully."
    }), 201


# company register
@auth.route("/api/company/register", methods=["POST"])
def register_company():

    # Get JSON data from request
    data = request.get_json()

    # Extract fields
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    discription = data.get("discription")

    # Validate required fields
    if not all([name, email, password, discription]):
        return jsonify({
            "message": "All required fields are mandatory."
        }), 400

    # Check if email already exists
    existing_company = Company.query.filter_by(email=email).first()

    if existing_company:
        return jsonify({
            "message": "Company already registered."
        }), 409

    # Hash password
    hashed_password = generate_password_hash(password)

    # Create Company object
    company = Company(
        name=name,
        email=email,
        password=hashed_password,
        discription=discription,
        is_approved=False,   # Admin approval required
        is_active=True
    )

    # Save to database
    db.session.add(company)
    db.session.commit()

    return jsonify({
        "message": "Company registered successfully. Waiting for admin approval."
    }), 201

@auth.route("/api/login", methods=["POST"])
def login():
    # recive data from frontend api
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "Email and Password are required."
        }), 400

# ADMIN 

    admin = Admin.query.filter_by(email=email).first()

    if admin and check_password_hash(admin.password, password):

        token = create_access_token(
            identity=str(admin.id),
            additional_claims={
                "role": "admin"
            }
        )

        return jsonify({
            "message": "Admin Login Successful",
            "token": token,
            "role": "admin",
            "redirect": "/admin/dashboard" # it will not directly redirect this will sends to the vue and the using vue router it will do it 
        }), 200

# STUDENT 

    student = Student.query.filter_by(email=email).first()

    if student and check_password_hash(student.password, password):

        token = create_access_token(
            identity=str(student.id),
            additional_claims={
                "role": "student"
            }
        )

        return jsonify({
            "message": "Student Login Successful",
            "token": token,
            "role": "student",
            "redirect": "/student/dashboard"
        }), 200
# company 
    company = Company.query.filter_by(email=email).first()

    if company:

        if not company.is_approved:

            return jsonify({
                "message": "Company is waiting for Admin approval."
            }), 403

        if check_password_hash(company.password, password):

            token = create_access_token(
                identity=str(company.id),
                additional_claims={
                    "role": "company"
                }
            )

            return jsonify({
                "message": "Company Login Successful",
                "token": token,
                "role": "company",
                "redirect": "/company/dashboard"
            }), 200

    return jsonify({
        "message": "Invalid Email or Password."
    }), 401


