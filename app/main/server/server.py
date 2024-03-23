from flask import Flask
from app.main.routes.meals import meals_route_bp
from app.main.database import database
from app.main.repository.meals import Meals


def create_app():
    app = Flask(__name__)

    database.init_app(app)
    app.register_blueprint(meals_route_bp)

    return app
