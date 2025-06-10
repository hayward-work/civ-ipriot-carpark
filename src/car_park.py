class CarPark:
    def __init__(self, location, capacity, all_cars=None, sensors=None,  displays=None):
        self.location = location
        self.capacity = sensors or []
        self.displays = displays or []
        self.all_cars = all_cars or {}

    def __str__(self):
        return f"{self.location} car park with {self.capacity} bays."

    def update_display(self):
        ...