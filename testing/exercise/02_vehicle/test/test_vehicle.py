from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    VALID_FUEL = 50
    VALID_HORSE_POWER = 200

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.VALID_FUEL, self.VALID_HORSE_POWER)

    def test_init__expect_to_set_correct_values(self):
        self.assertEqual(self.VALID_FUEL, self.vehicle.fuel)
        self.assertEqual(self.VALID_HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.VALID_FUEL, self.vehicle.capacity)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive__when_fuel_is_less_than_needed__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(context.exception))

    def test_drive__when_fuel_is_enough__expect_to_decrease_the_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_refuel__when_total_fuel_is_more_than_capacity__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(context.exception))

    def test_refuel__when_total_fuel_is_less_or_equal_to_capacity__expect_to_add_it(self):
        self.vehicle.fuel = 25
        self.vehicle.refuel(15)
        self.assertEqual(40, self.vehicle.fuel)

    def test_str__expect_correct_return(self):
        return_message = f"The vehicle has {self.VALID_HORSE_POWER} " \
               f"horse power with {self.VALID_FUEL} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(return_message, self.vehicle.__str__())


if __name__ == '__main__':
    unittest.main()
