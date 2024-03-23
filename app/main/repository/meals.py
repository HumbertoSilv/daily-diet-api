from app.main.database.database import db
from uuid import uuid4


class Meals(db.Model):
    id = db.Column(db.String(100), primary_key=True, default=uuid4())
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    name = db.Column(db.String(100))
    extra = db.Column(db.Boolean)
