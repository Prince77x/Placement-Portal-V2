from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from models import Student, Admin, Company, db, Job, Application
from cache import cache

admin = Blueprint('admin', __name__)


@admin.route("/api/admin/dashboard", methods=["GET"])
@jwt_required()
def admin_dashboard():

    current_user = get_jwt_identity()

    admin_user = Admin.query.get(current_user)

    companies = Company.query.all()

    students = Student.query.all()

    jobs = Job.query.all()

    applications = Application.query.all()

    return jsonify({

        "admin": {
            "id": admin_user.id,
            "name": admin_user.name
        },

        "companies": [
            {
                "id": company.id,
                "name": company.name,
                "discription": company.discription,
                "is_active": company.is_active,
                "is_approved": company.is_approved
            }
            for company in companies
        ],

        "students": [
            {
                "id": student.id,
                "name": student.name,
                "skills": student.skills,
                "resume": student.resume,
                "is_active": student.is_active
            }
            for student in students
        ],

        "jobs": [
            {
                "id": job.id,
                "drive": job.drive,
                "company_name": job.company.name,
                "is_approved": job.is_approved,
                "status": job.status
            }
            for job in jobs
        ],

        "applications": [
            {
                "id": application.id,

                "student": {
                    "id": application.student.id,
                    "name": application.student.name
                },

                "job": {
                    "id": application.job.id,

                    "company": {
                        "id": application.job.company.id,
                        "name": application.job.company.name
                    }
                }
            }
            for application in applications
        ]

    })


# Dashboard stats
@admin.route("/api/admin/stats", methods=["GET"])
@jwt_required()
def admin_stats():

    total_students = Student.query.count()
    total_companies = Company.query.count()
    total_jobs = Job.query.count()
    total_applications = Application.query.count()

    return jsonify({
        "total_students": total_students,
        "total_companies": total_companies,
        "total_jobs": total_jobs,
        "total_applications": total_applications
    })


# View one drive/job with its applications
@admin.route("/api/admin/job/<int:id>", methods=["GET"])
@jwt_required()
def admin_drive_details(id):

    job = Job.query.get_or_404(id)

    return jsonify({

        "job": {
            "id": job.id,
            "drive": job.drive,
            "title": job.title,
            "description": job.description,
            "skills_required": job.skills_required,
            "experience_required": job.experience_required,
            "salary_range": job.salary_range,
            "location": job.location,
            "status": job.status,
            "is_approved": job.is_approved,
            "company_name": job.company.name
        },

        "applications": [
            {
                "id": app.id,
                "student_name": app.student.name,
                "status": app.status
            }
            for app in job.applications
        ]

    })


# View one application in detail
@admin.route("/api/admin/application/<int:id>", methods=["GET"])
@jwt_required()
def admin_application_details(id):

    application = Application.query.get_or_404(id)

    return jsonify({
        "id": application.id,
        "status": application.status,
        "student": {
            "id": application.student.id,
            "name": application.student.name,
            "email": application.student.email,
            "skills": application.student.skills,
            "resume": application.student.resume
        },
        "job": {
            "id": application.job.id,
            "drive": application.job.drive,
            "title": application.job.title,
            "company_name": application.job.company.name
        }
    })


# Approve company
@admin.route("/api/company/<int:id>/approve", methods=["PUT"])
@jwt_required()
def approve_company(id):

    company = Company.query.get_or_404(id)

    company.is_approved = True

    db.session.commit()

    return jsonify({"message": "Company Approved"})


# Blacklist company
@admin.route("/api/company/<int:id>/blacklist", methods=["PUT"])
@jwt_required()
def blacklist_company(id):

    company = Company.query.get_or_404(id)

    company.is_active = False

    db.session.commit()

    return jsonify({"message": "Company Blacklisted"})


# Activate company
@admin.route("/api/company/<int:id>/activate", methods=["PUT"])
@jwt_required()
def activate_company(id):

    company = Company.query.get_or_404(id)

    company.is_active = True

    db.session.commit()

    return jsonify({"message": "Company Activated"})


# Remove company
@admin.route("/api/company/<int:id>/remove", methods=["DELETE"])
@jwt_required()
def remove_company(id):

    company = Company.query.get_or_404(id)

    if len(company.jobs) > 0:
        return jsonify({
            "message": "Cannot remove this company, it has job postings. Blacklist instead."
        }), 400

    db.session.delete(company)
    db.session.commit()

    return jsonify({"message": "Company removed"})


# Blacklist student
@admin.route("/api/student/<int:id>/blacklist", methods=["PUT"])
@jwt_required()
def blacklist_student(id):

    student = Student.query.get_or_404(id)

    student.is_active = False

    db.session.commit()

    return jsonify({"message": "Student Blacklisted"})


# Activate student
@admin.route("/api/student/<int:id>/activate", methods=["PUT"])
@jwt_required()
def activate_student(id):

    student = Student.query.get_or_404(id)

    student.is_active = True

    db.session.commit()

    return jsonify({"message": "Student Activated"})


# Remove student
@admin.route("/api/student/<int:id>/remove", methods=["DELETE"])
@jwt_required()
def remove_student(id):

    student = Student.query.get_or_404(id)

    if len(student.applications) > 0:
        return jsonify({
            "message": "Cannot remove this student, they have applications. Blacklist instead."
        }), 400

    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student removed"})


# Approve job posting
@admin.route("/api/job/<int:id>/approve", methods=["PUT"])
@jwt_required()
def approve_job(id):

    job = Job.query.get_or_404(id)

    job.is_approved = True

    db.session.commit()

    return jsonify({"message": "Job approved"})


# Remove job posting
@admin.route("/api/job/<int:id>/remove", methods=["DELETE"])
@jwt_required()
def remove_job(id):

    job = Job.query.get_or_404(id)

    if len(job.applications) > 0:
        return jsonify({
            "message": "Cannot remove this job, it already has applications. Close it instead."
        }), 400

    db.session.delete(job)
    db.session.commit()

    return jsonify({"message": "Job removed"})


# Mark drive as complete
@admin.route("/api/job/<int:id>/complete", methods=["PUT"])
@jwt_required()
def complete_drive(id):

    job = Job.query.get_or_404(id)

    job.status = "Closed"

    db.session.commit()

    return jsonify({"message": "Drive Completed"})


# Search
@admin.route("/api/admin/search")
@jwt_required()
@cache.cached(timeout=60, query_string=True)
def search():

    query = request.args.get("q", "")

    companies = Company.query.filter(
        Company.name.ilike(f"%{query}%")
    ).all()

    students = Student.query.filter(
        (Student.name.ilike(f"%{query}%")) |
        (Student.email.ilike(f"%{query}%"))
    ).all()

    return jsonify({

        "companies": [
            {"id": c.id, "name": c.name}
            for c in companies
        ],

        "students": [
            {"id": s.id, "name": s.name}
            for s in students
        ]

    })