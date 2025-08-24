from flask import Blueprint, request, jsonify
from .. import crud

activities_bp = Blueprint("activities", __name__)

@activities_bp.route("/activities", methods=["POST"])
def add_activity():
    data = request.json
    activity = crud.create_activity(data)
    return jsonify({"id": activity.id, "name": activity.name}), 201

@activities_bp.route("/activities", methods=["GET"])
def list_activities():
    activities = crud.get_activities()
    return jsonify([{"id": a.id, "name": a.name, "description": a.description} for a in activities])
