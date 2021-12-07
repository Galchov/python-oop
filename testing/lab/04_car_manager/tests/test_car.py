from project.car import Car

from unittest import TestCase, main


class TestCar(TestCase):
    valid_make = 'make'
    valid_model = 'model'
    valid_consumption = 10
    valid_capacity = 100

    def setUp(self):
        self.car = Car(self.valid_make, self.valid_model, self.valid_consumption, self.valid_capacity)

    def test_car_make_setter__when_None__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.make = None
        self.assertEqual('Make cannot be null or empty!', str(context.exception))

    def test_car_model_setter__when_None__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.model = None
        self.assertEqual('Model cannot be null or empty!', str(context.exception))

    def test_car_fuel_consumption_setter__when_zero__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(context.exception))

    def test_car_fuel_consumption_setter__when_less_than_zero__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -1
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(context.exception))

    def test_car_fuel_capacity_setter__when_zero__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(context.exception))

    def test_car_fuel_capacity_setter__when_less_than_zero__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -1
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(context.exception))

    def test_car_fuel_amount_setter__when_less_than_zero__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1
        self.assertEqual('Fuel amount cannot be negative!', str(context.exception))

    def test_car_refuel__when_zero__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(context.exception))

    def test_car_refuel__when_negative__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-1)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(context.exception))

    def test_car_refuel__when_positive__expect_exception(self):
        fuel = 30
        self.car.refuel(fuel)
        self.assertEqual(fuel, self.car.fuel_amount)

    def test_car_refuel__when_amount_greater_than_capacity__expect_to_equalize_them(self):
        expected_capacity = 100
        self.car.fuel_amount = 0

        self.car.refuel(120)

        self.assertEqual(expected_capacity, self.car.fuel_amount)

    def test_car_drive__when_needed_is_greater_than_the_current_amount__expect_exception(self):
        self.car.fuel_amount = 20
        self.car.fuel_consumption = 15

        with self.assertRaises(Exception) as context:
            self.car.drive(200)
        self.assertEqual('You don\'t have enough fuel to drive!', str(context.exception))


if __name__ == '__main__':
    main()
