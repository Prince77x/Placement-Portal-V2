from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, send_file
from celery_app import celery
from tasks import export_student_applications, export_company_data, generate_placement_report

export = Blueprint('export', __name__)


# Student triggers their own export
@export.route("/api/student/export", methods=["POST"])
@jwt_required()
def trigger_student_export():

    current_user = get_jwt_identity()

    task = export_student_applications.delay(current_user)

    return jsonify({"message": "Export started", "task_id": task.id})


# Company triggers their own export
@export.route("/api/company/export", methods=["POST"])
@jwt_required()
def trigger_company_export():

    current_user = get_jwt_identity()

    task = export_company_data.delay(current_user)

    return jsonify({"message": "Export started", "task_id": task.id})


# Company triggers their own placement report manually (instead of waiting for monthly job)
@export.route("/api/company/report", methods=["POST"])
@jwt_required()
def trigger_company_report():

    current_user = get_jwt_identity()

    task = generate_placement_report.delay(current_user)

    return jsonify({"message": "Report generation started", "task_id": task.id})


# Check status of any task (export or report)
@export.route("/api/task/<task_id>/status", methods=["GET"])
@jwt_required()
def task_status(task_id):

    task = celery.AsyncResult(task_id)

    if task.state == "PENDING":
        return jsonify({"state": task.state})

    if task.state == "SUCCESS":
        return jsonify({"state": task.state, "result": task.result})

    if task.state == "FAILURE":
        return jsonify({"state": task.state, "error": str(task.info)})

    return jsonify({"state": task.state})


# Download the finished file
@export.route("/api/task/<task_id>/download", methods=["GET"])
@jwt_required()
def download_file(task_id):

    task = celery.AsyncResult(task_id)

    if task.state != "SUCCESS":
        return jsonify({"message": "File not ready yet"}), 400

    file_path = task.result.get("file")

    if not file_path:
        return jsonify({"message": "No file found"}), 404

    return send_file(file_path, as_attachment=True)