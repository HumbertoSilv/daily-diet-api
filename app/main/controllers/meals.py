from flask import request, jsonify

from app.main.models.meals import Meal


def create_meal():
    data = request.get_json()
    name = data.get("name")
    extra = data.get("extra")
    date = data.get("date")

    if extra is None or not name or not date:
        return jsonify({"message": "invalid parameters"}), 400

    try:
        Meal(**data)
        return jsonify({"message": "success"}), 201

    except Exception:
        return jsonify({"message": "failed to save"}), 400
