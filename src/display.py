class Display:
    def __init__(self, id, car_park, message = "", is_on = "False"):
        self.id = id
        self.car_park = car_park
        self.message = message or ""
        self.is_on = is_on or False

    def __str__(self):
        return f"Display {self.id}: {self.message}"

    def update(self, data):
        for key, value in data.items():
            self.__dict__[key] = value