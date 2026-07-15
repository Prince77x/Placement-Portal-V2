from flask_jwt_extended import get_jwt_identity
from flask import Blueprint, jsonify, request
from models import Company, Job, Application, db
from utils import role_required

company = Blueprint('company', __name__)


@company.route("/api/company/dashboard", methods=["GET"])
@role_required("company")
def company_dashboard():

    current_user = get_jwt_identity()

    comp = Company.query.get(current_user)

    if not comp.is_approved:
        return jsonify({"message": "Your company is not approved yet"}), 403

    jobs = Job.query.filter_by(company_id=comp.id).all()

    return jsonify({

        "company": {
            "id": comp.id,
            "name": comp.name,
            "discription": comp.discription
        },

        "jobs": [
            {
                "id": job.id,
                "drive": job.drive,
                "title": job.title,
                "status": job.status
            }
            for job in jobs
        ]

    })


# Post a new job / drive
@company.route("/api/company/job", methods=["POST"])
@role_required("company")
def post_job():

    current_user = get_jwt_identity()

    comp = Company.query.get(current_user)

    if not comp.is_approved:
        return jsonify({"message": "Your company is not approved yet"}), 403

    data = request.get_json()

    job = Job(
        drive=data["drive"],
        title=data["title"],
        description=data.get("description"),
        skills_required=data.get("skills_required"),
        experience_required=data.get("experience_required"),
        salary_range=data.get("salary_range"),
        location=data.get("location"),
        company_id=comp.id
    )

    db.session.add(job)
    db.session.commit()

    return jsonify({"message": "Drive created successfully"})


# Mark a drive as complete/closed
@company.route("/api/company/job/<int:id>/complete", methods=["PUT"])
@role_required("company")
def mark_complete(id):

    job = Job.query.get_or_404(id)

    job.status = "Closed"

    db.session.commit()

    return jsonify({"message": "Drive marked as complete"})


# Reopen a closed drive
@company.route("/api/company/job/<int:id>/reopen", methods=["PUT"])
@role_required("company")
def reopen_drive(id):

    job = Job.query.get_or_404(id)

    job.status = "Open"

    db.session.commit()

    return jsonify({"message": "Drive reopened"})


# View applicants for a job
@company.route("/api/company/job/<int:id>/applicants", methods=["GET"])
@role_required("company")
def view_applicants(id):

    job = Job.query.get_or_404(id)

    return jsonify({

        "job": {
            "id": job.id,
            "title": job.title,
            "drive": job.drive
        },

        "applicants": [
            {
                "application_id": app.id,
                "status": app.status,
                "student": {
                    "id": app.student.id,
                    "name": app.student.name,
                    "email": app.student.email,
                    "skills": app.student.skills,
                    "resume": app.student.resume
                }
            }
            for app in job.applications
        ]

    })


# Shortlist an applicant
@company.route("/api/company/application/<int:id>/shortlist", methods=["PUT"])
@role_required("company")
def shortlist_applicant(id):

    application = Application.query.get_or_404(id)

    application.status = "Shortlisted"

    db.session.commit()

    return jsonify({"message": "Applicant shortlisted"})


# Reject an applicant
@company.route("/api/company/application/<int:id>/reject", methods=["PUT"])
@role_required("company")
def reject_applicant(id):

    application = Application.query.get_or_404(id)

    application.status = "Rejected"

    db.session.commit()

    return jsonify({"message": "Applicant rejected"})


# Select an applicant (final)
@company.route("/api/company/application/<int:id>/select", methods=["PUT"])
@role_required("company")
def select_applicant(id):

    application = Application.query.get_or_404(id)

    application.status = "Selected"

    db.session.commit()

    return jsonify({"message": "Applicant selected"})