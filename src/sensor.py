from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, id, car_park, is_active = False):
        self.id = id
        self.car_park = car_park
        self.is_active = is_active

    def __str__(self):
        return f"Sensor {self.id}, active status: {self.is_active}"

    @abstractmethod
    def update_car_park(self):
        ...

    @abstractmethod
    def scan_plate(self):
        ...

class EntrySensor(Sensor):
    def update_car_park(self):
        ...

class ExitSensor(Sensor):
    def update_car_park(self):
        ...