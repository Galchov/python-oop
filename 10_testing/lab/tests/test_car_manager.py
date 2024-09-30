from unittest import TestCase, main

from projects.car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Hyundai", "Tucson", 5, 40)

    def test_init(self):
        self.assertEqual("Hyundai", self.car.make)
        self.assertEqual("Tucson", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(40, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_set_make__empty_string__raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_set_model__empty_string__raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_set_fuel_consumption__less_than_or_equal_to_zero__raises(self):
        # Attempt with negative amount
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        # Attempt with zero
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_set_fuel_capacity__less_than_or_equal_to_zero__raises(self):
        # Attempt with negative amount
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        # Attempt with zero
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_set_fuel_amount__negative_value__raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel__less_than_or_equal_to_zero__raises(self):
        # Attempt with negative value
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

        # Attempt with zero
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

    def test_refuel__positive_value_less_than_capacity__increases_fuel(self):
        self.assertEqual(0, self.car.fuel_amount)

        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel_amount)

        self.car.refuel(20)
        self.assertEqual(25, self.car.fuel_amount)

    def test_refuel__greater_than_capacity__sets_to_capacity(self):
        self.assertEqual(0, self.car.fuel_amount)

        fuel_amount = self.car.fuel_capacity + 1
        self.car.refuel(fuel_amount)

        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_drive_not_enough_fuel_amount_raises(self):
        self.assertEqual(0, self.car.fuel_amount)

        needed = (10 / 100) * self.car.fuel_consumption
        needed += 1

        with self.assertRaises(Exception) as ex:
            self.car.drive(needed)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

        self.assertEqual(0, self.car.fuel_amount)

    def test_drive(self):
        distance = 10

        self.car.refuel(40)
        self.assertEqual(40, self.car.fuel_amount)
        self.car.drive(distance)

        expected = 39.5
        self.assertEqual(expected, self.car.fuel_amount)


if __name__ == "__main__":
    main()
