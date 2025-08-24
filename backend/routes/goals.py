from flask import Blueprint, request, jsonify
from .. import crud

goals_bp = Blueprint("goals", __name__)

@goals_bp.route("/goals", methods=["POST"])
def add_goal():
    data = request.json
    goal = crud.create_goal(data)
    return jsonify({"id": goal.id, "title": goal.title}), 201

@goals_bp.route("/goals", methods=["GET"])
def list_goals():
    goals = crud.get_goals()
    return jsonify([{"id": g.id, "title": g.title, "progress": g.progress, "period": g.period} for g in goals])
