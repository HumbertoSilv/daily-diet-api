from flask import Blueprint
from app.main.controllers.meals import (
    create_meal,
    update_meal_by_id,
    delete_meal_by_id
    )


meals_route_bp = Blueprint("meals_route", __name__, url_prefix="/api")


meals_route_bp.post("/meals")(create_meal)
meals_route_bp.patch("/meals/<string:id>")(update_meal_by_id)
meals_route_bp.delete("/meals/<string:id>")(delete_meal_by_id)
