import os
import csv
from datetime import datetime
from celery_app import celery
from models import Company, Job, Application, Student, Placement, db

REPORTS_DIR = "reports"
EXPORTS_DIR = "exports"

os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(EXPORTS_DIR, exist_ok=True)


# ---------- Placement Report ----------

@celery.task
def generate_placement_report(company_id):

    company = Company.query.get(company_id)

    if not company:
        return {"error": "Company not found"}

    jobs = Job.query.filter_by(company_id=company.id).all()

    total_jobs = len(jobs)
    total_applications = sum(len(job.applications) for job in jobs)

    placed_count = 0
    for job in jobs:
        for app in job.applications:
            if app.status == "Selected":
                placed_count += 1

    now = datetime.utcnow()
    filename = f"{REPORTS_DIR}/company_{company.id}_{now.year}_{now.month}.html"

    html = f"""
    <html>
    <head><title>Placement Report - {company.name}</title></head>
    <body>
        <h1>Placement Report: {company.name}</h1>
        <p>Generated on: {now.strftime('%Y-%m-%d %H:%M')}</p>
        <p>Total Job Postings: {total_jobs}</p>
        <p>Total Applications Received: {total_applications}</p>
        <p>Total Students Placed: {placed_count}</p>

        <h2>Job-wise Breakdown</h2>
        <table border="1" cellpadding="8">
            <tr><th>Drive</th><th>Title</th><th>Status</th><th>Applications</th></tr>
    """

    for job in jobs:
        html += f"<tr><td>{job.drive}</td><td>{job.title}</td><td>{job.status}</td><td>{len(job.applications)}</td></tr>"

    html += """
        </table>
    </body>
    </html>
    """

    with open(filename, "w") as f:
        f.write(html)

    # Placeholder for the "notify company" step - swap this for real email/SMS later
    print(f"[NOTIFY] Placement report ready for {company.name} at {filename}")

    return {"company": company.name, "file": filename}


@celery.task
def generate_all_placement_reports():

    companies = Company.query.filter_by(is_approved=True).all()

    for company in companies:
        generate_placement_report.delay(company.id)

    return {"message": f"Triggered reports for {len(companies)} companies"}


# ---------- CSV Export ----------

@celery.task
def export_student_applications(student_id):

    student = Student.query.get(student_id)

    if not student:
        return {"error": "Student not found"}

    applications = Application.query.filter_by(student_id=student.id).all()

    now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{EXPORTS_DIR}/student_{student.id}_{now}.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Drive", "Job Title", "Company", "Status"])

        for app in applications:
            writer.writerow([
                app.job.drive,
                app.job.title,
                app.job.company.name,
                app.status
            ])

    # Placeholder for the "notify user their export is ready" step
    print(f"[NOTIFY] CSV export ready for student {student.name} at {filename}")

    return {"file": filename}


@celery.task
def export_company_data(company_id):

    company = Company.query.get(company_id)

    if not company:
        return {"error": "Company not found"}

    jobs = Job.query.filter_by(company_id=company.id).all()

    now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{EXPORTS_DIR}/company_{company.id}_{now}.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Drive", "Job Title", "Student", "Status"])

        for job in jobs:
            for app in job.applications:
                writer.writerow([
                    job.drive,
                    job.title,
                    app.student.name,
                    app.status
                ])

    print(f"[NOTIFY] CSV export ready for company {company.name} at {filename}")

    return {"file": filename}