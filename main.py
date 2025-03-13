class Duration:
    def __init__(self, hours, minutes):
        self.__hours = hours
        self.__minutes = minutes

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        self.__hours = value

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        self.__minutes = value

    def __str__(self):
        return f"{self.__hours:02d}:{self.__minutes:02d}"

    def get_duration_in_minutes(self):
        return self.__hours * 60 + self.__minutes

    def __add__(self, minutes_to_add):
        total_minutes = self.get_duration_in_minutes() + minutes_to_add
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return Duration(hours, minutes)

duration = Duration(5, 30)

print(f"Тривалість у форматі __str__: {duration}")

print(f"Тривалість в хвилинах: {duration.get_duration_in_minutes()}")

new_duration = duration + 40
print(f"Тривалість після додавання 40 хвилин: {new_duration}")
