from flask import Blueprint, request, jsonify
from .. import crud

sessions_bp = Blueprint("sessions", __name__)

@sessions_bp.route("/sessions", methods=["POST"])
def add_session():
    data = request.json
    session = crud.create_session(data)
    return jsonify({"id": session.id, "activity_id": session.activity_id}), 201

@sessions_bp.route("/sessions", methods=["GET"])
def list_sessions():
    sessions = crud.get_sessions()
    return jsonify([{"id": s.id, "activity_id": s.activity_id, "start_time": s.start_time.isoformat(), "end_time": s.end_time.isoformat() if s.end_time else None} for s in sessions])
