from display import Display
from sensor import Sensor


class CarPark:
    def __init__(self, location, capacity, all_cars=None, sensors=None,  displays=None):
        self.location = location
        self.capacity = capacity
        self.sensors = sensors or []
        self.displays = displays or []
        self.all_cars = all_cars or {}

    def __str__(self):
        return f"{self.location} car park with {self.capacity} bays."

    def register(self, reference):
        match reference:
            case Sensor():
                self.sensors.append(reference)
            case Display():
                self.displays.append(reference)



    def update_displays(self):
        ...