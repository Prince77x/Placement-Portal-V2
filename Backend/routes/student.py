from flask_jwt_extended import get_jwt_identity
from flask import Blueprint, jsonify, request
from models import Student, Company, Job, Application, db
from cache import cache
from utils import role_required

student = Blueprint('student', __name__)


@student.route("/api/student/dashboard", methods=["GET"])
@role_required("student")
def student_dashboard():

    current_user = get_jwt_identity()

    stu = Student.query.get(current_user)

    companies = Company.query.filter_by(is_approved=True, is_active=True).all()

    applications = Application.query.filter_by(student_id=stu.id).all()

    return jsonify({

        "student": {
            "id": stu.id,
            "name": stu.name,
            "email": stu.email,
            "education": stu.education,
            "skills": stu.skills,
            "resume": stu.resume
        },

        "companies": [
            {
                "id": company.id,
                "name": company.name
            }
            for company in companies
        ],

        "applications": [
            {
                "id": app.id,
                "drive": app.job.drive,
                "company_name": app.job.company.name,
                "status": app.status,
                "job_id": app.job_id
            }
            for app in applications
        ]

    })


# View a single company and its open jobs
@student.route("/api/student/company/<int:id>", methods=["GET"])
@role_required("student")
def company_detail(id):

    company = Company.query.get_or_404(id)

    jobs = Job.query.filter_by(company_id=company.id, status="Open").all()

    return jsonify({

        "company": {
            "id": company.id,
            "name": company.name,
            "discription": company.discription
        },

        "jobs": [
            {
                "id": job.id,
                "drive": job.drive,
                "title": job.title,
                "skills_required": job.skills_required
            }
            for job in jobs
        ]

    })


# Search / list job postings
@student.route("/api/student/jobs", methods=["GET"])
@role_required("student")
@cache.cached(timeout=60, query_string=True)
def list_jobs():

    query = request.args.get("q", "")

    jobs = Job.query.filter(
        Job.status == "Open",
        (Job.title.ilike(f"%{query}%")) |
        (Job.skills_required.ilike(f"%{query}%"))
    ).all()

    return jsonify([
        {
            "id": job.id,
            "drive": job.drive,
            "title": job.title,
            "company_name": job.company.name,
            "skills_required": job.skills_required,
            "experience_required": job.experience_required,
            "salary_range": job.salary_range,
            "location": job.location
        }
        for job in jobs
    ])


# View full details of one job/drive
@student.route("/api/student/job/<int:id>", methods=["GET"])
@role_required("student")
def view_drive(id):

    job = Job.query.get_or_404(id)

    return jsonify({
        "id": job.id,
        "drive": job.drive,
        "title": job.title,
        "description": job.description,
        "skills_required": job.skills_required,
        "experience_required": job.experience_required,
        "salary_range": job.salary_range,
        "location": job.location,
        "company_name": job.company.name,
        "status": job.status
    })


# Apply for a job
@student.route("/api/student/job/<int:id>/apply", methods=["POST"])
@role_required("student")
def apply_job(id):

    current_user = get_jwt_identity()

    job = Job.query.get_or_404(id)

    if job.status != "Open":
        return jsonify({"message": "This drive is closed"}), 400

    existing = Application.query.filter_by(student_id=current_user, job_id=id).first()

    if existing:
        return jsonify({"message": "You have already applied to this drive"}), 400

    application = Application(
        student_id=current_user,
        job_id=id
    )

    db.session.add(application)
    db.session.commit()

    return jsonify({"message": "Applied successfully"})


# View one application in detail (status + placement info if selected)
@student.route("/api/student/application/<int:id>", methods=["GET"])
@role_required("student")
def view_application(id):

    application = Application.query.get_or_404(id)

    placement_info = None

    if application.placement:
        placement = application.placement[0]
        placement_info = {
            "offer_date": placement.offer_date.isoformat() if placement.offer_date else None,
            "joining_date": placement.joining_date.isoformat() if placement.joining_date else None,
            "package": placement.package
        }

    return jsonify({
        "id": application.id,
        "status": application.status,
        "drive": application.job.drive,
        "job_title": application.job.title,
        "company_name": application.job.company.name,
        "placement": placement_info
    })


# Update profile
@student.route("/api/student/profile", methods=["PUT"])
@role_required("student")
def update_profile():

    current_user = get_jwt_identity()

    stu = Student.query.get(current_user)

    data = request.get_json()

    stu.education = data.get("education", stu.education)
    stu.skills = data.get("skills", stu.skills)
    stu.resume = data.get("resume", stu.resume)

    db.session.commit()

    return jsonify({"message": "Profile updated"})