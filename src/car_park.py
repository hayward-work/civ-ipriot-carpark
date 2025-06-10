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

    def register(self, component):
        match component:
            case Sensor():
                self.sensors.append(component)
            case Display():
                self.displays.append(component)
            case _:
                raise TypeError("Object must be of type Sensor or Display")

    def add_car(self, plate):
        self.all_cars.add(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.all_cars.remove(plate)
        # Change to use .discard() if issues arise
        self.update_displays()

    def update_displays(self):
        for i in self.displays:
            i.update()