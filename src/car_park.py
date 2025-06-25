import json
from pathlib import Path
from datetime import datetime
from display import Display
from sensor import Sensor


class CarPark:
    def __init__(self, location, capacity, all_cars=None, sensors=None,  displays=None, log_file=Path("log.txt"), config_file=Path("config.json")):
        self.location = location
        self.capacity = capacity
        self.sensors = sensors or []
        self.displays = displays or []
        self.cars = all_cars or set()
        self.log_file = log_file if isinstance(log_file, Path) else Path("log.txt")
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file if isinstance(config_file, Path) else Path("config.json")
        self.config_file.touch(exist_ok=True)

    def __str__(self):
        return f"{self.location} car park with {self.capacity} bays."

    def _log_car_activity(self, plate, action):
        """
        Writes activity to log file specified by path stored in ``log_file``.
        :param plate: car license plate action was performed upon.
        :type plate: str
        :param action: performed action being logged.
        :type action: str
        """
        with self.log_file.open("a") as log:
            log.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def register(self, component):
        match component:
            case Sensor():
                self.sensors.append(component)
            case Display():
                self.displays.append(component)
            case _:
                raise TypeError("Object must be of type Sensor or Display")


    def add_car(self, plate):
        self.cars.add(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.cars.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    def update_displays(self):
        info = {"occupancy": self.occupancy,
                "temperature": self.temperature,}
        for i in self.displays:
            i.update(info)

    @property
    def occupancy(self):
        occupancy = self.capacity - len(self.cars)
        if occupancy > 0:
            return occupancy
        else:
            return 0

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

    def write_config(self):
        with self.config_file.open("w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    temperature = 25