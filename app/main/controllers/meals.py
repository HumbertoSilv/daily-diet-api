from flask import current_app, jsonify, request

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

        if not len(data.keys()) or not id:
            raise Exception("Invalid parameters")

        meal = Meals.query.get_or_404(id)

        for key, value in data.items():
            setattr(meal, key, value)

        current_app.db.session.commit()

        return jsonify({"message": "success"}), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 400


def delete_meal_by_id(id):
    try:
        if not id:
            raise Exception("Invalid parameters")

        meal = Meals.query.get_or_404(id)

        current_app.db.session.delete(meal)
        current_app.db.session.commit()

        return jsonify({"message": "success"}), 200

    except Exception as e:
        print(e)
        return jsonify({"message": str(e)}), 400
