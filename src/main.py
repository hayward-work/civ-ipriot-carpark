from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
def main():
    # TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
    car_park = CarPark("Moondalup", 100, log_file="moondalup.txt")

    # TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
    entry_sensor = EntrySensor(1, car_park, True)
    car_park.register(entry_sensor)

    # TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
    exit_sensor = ExitSensor(2, car_park, True)
    car_park.register(exit_sensor)

    # TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
    display = Display(1, car_park, "Welcome to Moondalup", True)
    car_park.register(display)

    # TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
    for i in range(10):
        entry_sensor.detect_car()

    # TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
    for i in range(2):
        exit_sensor.detect_car()

    if __name__ == main:
        main()