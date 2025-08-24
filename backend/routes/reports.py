from flask import Blueprint, request, jsonify
from .. import crud

reports_bp = Blueprint("reports", __name__)

@reports_bp.route("/reports", methods=["POST"])
def add_report():
    data = request.json
    report = crud.create_report(data)
    return jsonify({"id": report.id, "title": report.title}), 201

@reports_bp.route("/reports", methods=["GET"])
def list_reports():
    reports = crud.get_reports()
    return jsonify([{"id": r.id, "title": r.title, "created_at": r.created_at.isoformat()} for r in reports])
