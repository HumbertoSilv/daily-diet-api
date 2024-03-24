from flask import Blueprint
from app.main.controllers.meals import create_meal


meals_route_bp = Blueprint("meals_route", __name__, url_prefix="/api")


meals_route_bp.post("/meals")(create_meal)
