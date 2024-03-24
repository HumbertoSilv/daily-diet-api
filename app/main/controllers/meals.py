from flask import request, jsonify

from app.main.models.meals import Meal


def create_meal():
    data = request.get_json()

    if "name" not in data.keys() or "extra" not in data.keys():
        return jsonify({"message": "invalid parameters"}), 400

    try:
        Meal(**data)
        return jsonify({"message": "success"}), 201

    except Exception:
        return jsonify({"message": "failed to save"}), 400
