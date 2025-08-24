from flask import Blueprint, request, jsonify
from .. import crud

reminders_bp = Blueprint("reminders", __name__)

@reminders_bp.route("/reminders", methods=["POST"])
def add_reminder():
    data = request.json
    reminder = crud.create_reminder(data)
    return jsonify({"id": reminder.id, "message": reminder.message}), 201

@reminders_bp.route("/reminders", methods=["GET"])
def list_reminders():
    reminders = crud.get_reminders()
    return jsonify([{"id": r.id, "message": r.message, "time": r.time.isoformat()} for r in reminders])
