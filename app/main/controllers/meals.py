from flask import request, jsonify, current_app

from app.main.models.meals import Meal
from app.main.repository.meals import Meals


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


def update_meal_by_id(id):
    try:
        data = request.get_json()

        if not len(data.keys()) or id is None:
            raise Exception("Invalid parameters")

        meal = Meals.query.get_or_404(id)

        for key, value in data.items():
            setattr(meal, key, value)

        current_app.db.session.commit()

        return jsonify({"message": "success"}), 200

    except Exception as e:
        print(e)
        return jsonify({"message": str(e)}), 400
