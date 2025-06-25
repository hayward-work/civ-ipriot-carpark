from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


def main():
    # Creates an instance of `CarPark` from config json file using a class method.
    car_park = CarPark.from_config()

    entry_sensor = EntrySensor(1, car_park, True)

    exit_sensor = ExitSensor(2, car_park, True)

    display = Display(1, car_park, "Welcome to Moondalup", True)

    for i in range(10):
        entry_sensor.detect_car()

    for i in range(2):
        exit_sensor.detect_car()


if __name__ == "__main__":
    main()
