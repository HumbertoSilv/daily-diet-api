from datetime import date as datetime
from app.main.repository.meals import Meals


class Meal:
    def __init__(
            self,
            name: str,
            extra: bool,
            date: datetime,
            description: str = ""
            ) -> None:
        self.name = name
        self.extra = extra
        self.description = description
        self.date = datetime.fromisoformat(date)

        self.__create_meal()

    def __create_meal(self) -> None:
        new_meal = Meals(
            name=self.name,
            description=self.description,
            date=self.date,
            extra=self.extra
            )

        new_meal.save()
