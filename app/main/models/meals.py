from datetime import datetime, timezone
from app.main.repository.meals import Meals


class Meal:
    def __init__(self, name: str, extra: bool, description: str = "") -> None:
        self.name = name
        self.extra = extra
        self.description = description
        self.date = datetime.now(timezone.utc)

        self.__create_meal()

    def __create_meal(self):
        new_meal = Meals(
            name=self.name,
            description=self.description,
            date=self.date,
            extra=self.extra
            )

        new_meal.save()
