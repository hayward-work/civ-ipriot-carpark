import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("nowhere", 1)
        self.entry_sensor = EntrySensor(1, self.car_park, True)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)

    def test_detect_car(self):
        self.entry_sensor.detect_car()
        self.assertIsNot(self.car_park.cars, None)

if __name__ == "__main__":
    unittest.main()